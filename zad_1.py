class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def is_passed(self):
        average_marks = sum(self.marks) / len(self.marks)
        return average_marks > 50




# Przykładowe obiekty klasy Student
student1 = Student("Jan Kowalski", [60, 70, 80])
student2 = Student("Anna Nowak", [40, 45, 30])

# Testowanie metody is_passed
result1 = student1.is_passed()
result2 = student2.is_passed()

# Wyświetlenie wyników
print(f"{student1.name}: {'Zaliczony' if result1 else 'Nie zaliczony'}")
print(f"{student2.name}: {'Zaliczony' if result2 else 'Nie zaliczony'}")
