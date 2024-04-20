# import pika

# params = pika.URLParameters('amqps://woqqzdfw:yB1qus3DYDHTFimwiycxmB0HGZEPDGwZ@puffin.rmq2.cloudamqp.com/woqqzdfw')

# connection = pika.BlockingConnection(params)

# channel = connection.channel()

# def publish():
#     channel.basic_publish(exchange='', routing_key='product_management', body='hello')