import pika

params = pika.URLParameters('amqps://woqqzdfw:yB1qus3DYDHTFimwiycxmB0HGZEPDGwZ@puffin.rmq2.cloudamqp.com/woqqzdfw')

connection = pika.BlockingConnection(params)
channel = connection.channel()

def publish(product_id):
    message = f"Product added to cart: {product_id}"
    channel.basic_publish(exchange='', routing_key='admin', body=message)
    print(f" [x] Sent {message}")
