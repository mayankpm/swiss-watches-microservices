import pika
from cart.settings import RABBITMQ_HOST, RABBITMQ_PORT, RABBITMQ_USERNAME, RABBITMQ_PASSWORD, RABBITMQ_VHOST

class RabbitMQProducer:
    def __init__(self):
        credentials = pika.PlainCredentials(RABBITMQ_USERNAME, RABBITMQ_PASSWORD)
        self.connection = pika.BlockingConnection(pika.ConnectionParameters(host=RABBITMQ_HOST, port=RABBITMQ_PORT, virtual_host=RABBITMQ_VHOST, credentials=credentials))
        self.channel = self.connection.channel()

    def send_message(self, message, queue_name):
        self.channel.queue_declare(queue=queue_name)
        self.channel.basic_publish(exchange='', routing_key=queue_name, body=message)
        print(f"Sent '{message}' to '{queue_name}'")
        self.connection.close()
