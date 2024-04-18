import pika
from cart.settings import RABBITMQ_HOST, RABBITMQ_PORT, RABBITMQ_USERNAME, RABBITMQ_PASSWORD, RABBITMQ_VHOST

class RabbitMQConsumer:
    def __init__(self, queue_name):
        credentials = pika.PlainCredentials(RABBITMQ_USERNAME, RABBITMQ_PASSWORD)
        self.connection = pika.BlockingConnection(pika.ConnectionParameters(host=RABBITMQ_HOST, port=RABBITMQ_PORT, virtual_host=RABBITMQ_VHOST, credentials=credentials))
        self.channel = self.connection.channel()
        self.channel.queue_declare(queue=queue_name)
        self.channel.basic_consume(queue=queue_name, on_message_callback=self.callback, auto_ack=True)

    def callback(self, ch, method, properties, body):
        print(f"Received '{body.decode()}' from '{method.routing_key}'")

    def start_consuming(self):
        print('Waiting for messages. To exit press CTRL+C')
        self.channel.start_consuming()
