import pika
import json

# Connect to RabbitMQ
credentials = pika.PlainCredentials('my_user', 'my_password')
parameters = pika.ConnectionParameters('localhost', 5672, '/', credentials)
connection = pika.BlockingConnection(parameters)
channel = connection.channel()

# Declare the queue
channel.queue_declare(queue='watch_data_queue')

# Publish watch data
watch_data = {
    'watch_id': 1,
    'brand': 'Example Brand',
    'model': 'Example Model',
    'price': 100.0
}
channel.basic_publish(
    exchange='',
    routing_key='watch_data_queue',
    body=json.dumps(watch_data)
)

print(" [x] Sent watch data")

# Close the connection
connection.close()

