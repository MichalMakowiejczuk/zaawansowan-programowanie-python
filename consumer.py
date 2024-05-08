# consumer.py
import time

def read_from_file(filename):
    with open(filename, 'r') as file:
        lines = file.readlines()
    return lines

def update_status(filename, work_id, new_status):
    lines = read_from_file(filename)
    with open(filename, 'w') as file:
        for line in lines:
            if line.startswith(f"Praca {work_id}"):
                file.write(f"Praca {work_id},status:{new_status}\n")
            else:
                file.write(line)

def main():
    while True:
        # Odczytanie pracy z pliku
        lines = read_from_file('work.txt')
        for line in lines:
            if "status:pending" in line:
                work_id = line.split(',')[0].split()[1]
                print(f"Znaleziono pracę do wykonania: {work_id}")
                
                # Aktualizacja statusu na 'in_progress'
                update_status('work.txt', work_id, 'in_progress')
                
                # Symulacja wykonania pracy
                print(f"Rozpoczęcie pracy {work_id}")
                time.sleep(30)  # Symulacja wykonania pracy przez 30 sekund
                
                # Aktualizacja statusu na 'done' po wykonaniu pracy
                update_status('work.txt', work_id, 'done')
                print(f"Zakończono pracę {work_id}")
        
        # Pauza przed ponownym sprawdzeniem pracy
        time.sleep(5)

if __name__ == "__main__":
    main()
