import pika
import time
from config import RABBITMQ_HOST, RABBITMQ_PORT, RABBITMQ_USER, RABBITMQ_PASS

def update_status(work_id, new_status):
    # Tutaj możesz dodać logikę aktualizacji statusu pracy
    print(f"Aktualizacja statusu pracy {work_id} na: {new_status}")

def callback(ch, method, properties, body):
    # Przetwarzanie otrzymanej pracy
    work_data = body.decode('utf-8')
    work_id = work_data.split(',')[0].split()[1]
    print(f"Otrzymano pracę do wykonania: {work_id}")
    
    # Symulacja wykonania pracy
    print(f"Rozpoczęcie pracy {work_id}")
    time.sleep(21)  # Symulacja wykonania pracy przez 30 sekund
    
    # Aktualizacja statusu po wykonaniu pracy
    update_status(work_id, 'done')
    print(f"Zakończono pracę {work_id}")

def main():
    # Połączenie z serwerem RabbitMQ
    credentials = pika.PlainCredentials(RABBITMQ_USER, RABBITMQ_PASS)
    connection = pika.BlockingConnection(pika.ConnectionParameters(RABBITMQ_HOST, RABBITMQ_PORT, '/', credentials))
    channel = connection.channel()

    # Deklaracja kolejki
    channel.queue_declare(queue='prace')

    # Zarejestrowanie funkcji do obsługi otrzymanych wiadomości
    channel.basic_consume(queue='prace', on_message_callback=callback, auto_ack=True)

    print('Czekam na wiadomości...')
    # Rozpoczęcie nasłuchiwania wiadomości
    channel.start_consuming()

    # Zamknięcie połączenia
    connection.close()

if __name__ == "__main__":
    main()
