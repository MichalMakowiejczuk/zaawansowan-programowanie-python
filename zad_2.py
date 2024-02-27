class Employee:
    def __init__(self, first_name, last_name, hire_date, birth_date, city, street, zip_code, phone):
        self.first_name = first_name
        self.last_name = last_name
        self.hire_date = hire_date
        self.birth_date = birth_date
        self.city = city
        self.street = street
        self.zip_code = zip_code
        self.phone = phone

    def __str__(self):
        return (
            f"Employee Information:\n"
            f"Name: {self.first_name} {self.last_name}\n"
            f"Hire Date: {self.hire_date}\n"
            f"Birth Date: {self.birth_date}\n"
            f"City: {self.city}\n"
            f"Street: {self.street}\n"
            f"Zip code: {self.zip_code}\n"
            f"Phone: {self.phone}"
        )


class Order:
    def __init__(self, employee, student, books, order_date):
        self.employee = employee
        self.student = student
        self.books = books
        self.order_date = order_date

    def __str__(self):
        book_list = "\n".join([f"   - {book.title} by {book.author_name} {book.author_surname}" for book in self.books])
        return f"Order Details:\nEmployee: {self.employee}\nStudent: {self.student}\nBooks:\n{book_list}\nOrder Date: {self.order_date}"



class Book:
    def __init__(self, title, publication_date, author_name, author_surname, number_of_pages):
        self.title = title
        self.publication_date = publication_date
        self.author_name = author_name
        self.author_surname = author_surname
        self.number_of_pages = number_of_pages

    def __str__(self):
        return f"Title: {self.title}\nPublication Date: {self.publication_date}\nAuthor: {self.author_name} {self.author_surname}\nNumber of Pages: {self.number_of_pages}"


class Library:
    def __init__(self, city, street, zip_code, open_hours, phone):
        self.city = city
        self.street = street
        self.zip_code = zip_code
        self.open_hours = open_hours
        self.phone = phone
        self.books = []  # Lista książek w bibliotece

    def __str__(self):
        library_info = (
            f"Library Information:\n"
            f"City: {self.city}\n"
            f"Street: {self.street}\n"
            f"ZIP Code: {self.zip_code}\n"
            f"Open Hours: {self.open_hours}\n"
            f"Phone: {self.phone}\n"
        )

        books_info = "\nBooks in the Library:\n"
        if not self.books:
            books_info += "No books available."
        else:
            books_info += "\n".join(str(book) for book in self.books)

        return library_info + books_info

    def add_book(self, book):
        self.books.append(book)

# Przykład użycia:
library_example = Library(
    city="Example City",
    street="Main Street",
    zip_code="12345",
    open_hours="9:00 AM - 5:00 PM",
    phone="123-456-7890"
)

# books
book1 = Book(title="Introduction to Python", publication_date=2000, author_name="John", author_surname="Doe", number_of_pages=100)
book2 = Book(title="Intermidiet Python", publication_date=2001, author_name="John", author_surname="Doe", number_of_pages=200)
book3 = Book(title="Semi Intermidiet Python", publication_date=2004, author_name="John", author_surname="Doe", number_of_pages=500)
book4 = Book(title="Advance Python", publication_date=2006, author_name="John", author_surname="Doe", number_of_pages=300)
book5 = Book(title="Semi Advance Python", publication_date=2007, author_name="John", author_surname="Doe", number_of_pages=700)

# libraries
library1 = Library(city="Katowice", street="uliczna", zip_code="23343", open_hours="9-17", phone="213-231-432")
library2 = Library(city="Gliwice", street="fajna", zip_code="56789", open_hours="10-18", phone="218-643-890")

# employee
employee1 = Employee(first_name="Ja", last_name="nazwisko", hire_date="2020", birth_date="1970", city="Katowice", street="pogodna", zip_code="43213", phone="543-234-234")
employee2 = Employee(first_name="Ja", last_name="nazwisko", hire_date="2020", birth_date="1970", city="Katowice", street="pogodna", zip_code="43213", phone="543-234-234")
employee23 = Employee(first_name="Ja", last_name="nazwisko", hire_date="2020", birth_date="1970", city="Katowice", street="pogodna", zip_code="43213", phone="543-234-234")
library_example.add_book(book1)
library_example.add_book(book2)

print(library_example)

