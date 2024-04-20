import pika
import requests
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry

# RabbitMQ connection setup
params = pika.URLParameters('amqps://woqqzdfw:yB1qus3DYDHTFimwiycxmB0HGZEPDGwZ@puffin.rmq2.cloudamqp.com/woqqzdfw')
connection = pika.BlockingConnection(params)
channel = connection.channel()

channel.queue_declare(queue='admin')

def callback(ch, method, properties, body):
    print('Received in admin')
    print(body)
    # Assuming the message format is "Product added to cart: <product_id>"
    product_id = body.decode().split(": ")[1]
    
    # Configure retries
    session = requests.Session()
    retries = Retry(total=5, backoff_factor=0.1, status_forcelist=[500, 502, 503, 504])
    session.mount('http://', HTTPAdapter(max_retries=retries))
    session.mount('https://', HTTPAdapter(max_retries=retries))
    
    # Prepare the data to be sent
    data = {'product_id': product_id}
    
    # Perform the POST request
    try:
        response = session.post('http://web:8002/auth/cart/', json=data)
        response.raise_for_status() # Raises an HTTPError if the response was unsuccessful
        print(f"POST request successful: {response.text}")
    except requests.exceptions.RequestException as e:
        print(f"Failed to send POST request: {e}")

channel.basic_consume(queue='admin', on_message_callback=callback, auto_ack=True)

print('Started Consuming')

channel.start_consuming()

channel.close()