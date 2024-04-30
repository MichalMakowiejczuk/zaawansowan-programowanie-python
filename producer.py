# producer.py
import time
import random

def write_to_file(filename, data):
    with open(filename, 'a') as file:
        file.write(data + '\n')

def main():
    while True:
        # Generowanie przykładowej pracy (rozmowy telefonicznej)
        work_id = random.randint(1000, 9999)
        work_data = f"Praca {work_id},status:pending"
        
        # Zapis pracy do pliku
        write_to_file('work.txt', work_data)
        print(f"Zapisano pracę {work_id}")
        
        # Pauza przed dodaniem kolejnej pracy
        time.sleep(10)  # Pauza 10 sekund przed dodaniem kolejnej pracy

if __name__ == "__main__":
    main()


