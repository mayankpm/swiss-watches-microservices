import pika
import json

# Connect to RabbitMQ
credentials = pika.PlainCredentials('my_user', 'my_password')
parameters = pika.ConnectionParameters('localhost', 5672, '/', credentials)
connection = pika.BlockingConnection(parameters)
channel = connection.channel()

# Declare the queue
channel.queue_declare(queue='watch_data_queue')

def callback(ch, method, properties, body):
    watch_data = json.loads(body)
    print(" [x] Received watch data:", watch_data)

# Consume messages
channel.basic_consume(queue='watch_data_queue', on_message_callback=callback, auto_ack=True)

print(' [*] Waiting for watch data. To exit press CTRL+C')
channel.start_consuming()
