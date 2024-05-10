import pika

connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()
channel.queue_declare(queue='hello')

for _ in range(10000):
    channel.basic_publish(exchange='',
                        routing_key='hello',
                        body='Hello World!')

print(" [X] Sent 'Hello World!'")

connection.close()