import pika
import time
import random
from config import RABBITMQ_HOST, RABBITMQ_PORT, RABBITMQ_USER, RABBITMQ_PASS

def main():
    # Połączenie z serwerem RabbitMQ
    credentials = pika.PlainCredentials(RABBITMQ_USER, RABBITMQ_PASS)
    connection = pika.BlockingConnection(pika.ConnectionParameters(RABBITMQ_HOST, RABBITMQ_PORT, '/', credentials))
    channel = connection.channel()

    # Deklaracja kolejki
    channel.queue_declare(queue='prace')

    while True:
        # Generowanie przykładowej pracy (rozmowy telefonicznej)
        work_id = random.randint(1000, 9999)
        work_data = f"Praca {work_id}, status: pending"
        
        # Wysłanie pracy do kolejki
        channel.basic_publish(exchange='', routing_key='prace', body=work_data)
        print(f"Wysłano pracę {work_id} do kolejki")
        
        # Pauza przed dodaniem kolejnej pracy
        time.sleep(10)  # Pauza 10 sekund przed dodaniem kolejnej pracy

    # Zamknięcie połączenia
    connection.close()

if __name__ == "__main__":
    main()




