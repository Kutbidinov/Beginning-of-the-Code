

"""
Создайте класс Book с атрибутами title (название), author (автор) .
 И с методом display_info который печатает всю информацию по книге

Создайте класс Library, который будет содержать список книг в атрибуте books.
В классе Library реализуйте методы add_book(), remove_book(), find_book_by_title(), find_book_by_author(), и list_books().
"""


class Book:

    def __init__(self, title_pm: str, author_pm: str):
        self.title = title_pm
        self.author = author_pm


class Library:
    def __init__(self):
        self.books = []

    def add_book(self, new_book: Book):
        self.books.append(new_book)

    def list_books(self):
        return self.books

    def remove_book(self, rem_book: Book):
        self.books.remove(rem_book)

    def find_book_by_title(self, book_title: str):
        for item in self.books:
            if item.title == book_title:
                return item

    def find_book_by_author(self, author_name: str):
        for item in self.books:
            if item.author == author_name:
                return item


book1 = Book("Война и мир", "Л. Н. Толстой")
book2 = Book("Преступление и наказание", "Ф. М. Достоевский")

lib = Library()

lib.add_book(book2)
print(lib.list_books())  # [book2]
lib.add_book(book1)
print(lib.list_books())  # [book2, book1]

lib.remove_book(book2)
print(lib.list_books())  # [book1]

lib.find_book_by_title("Война и мир")  # book1
lib.find_book_by_title("БлаБла")  # None

lib.add_book(book1)


"""
Задание: Создание классов для управления сотрудниками и компанией

Описание задания:

Создайте класс Worker:
Атрибуты:
    name (имя сотрудника)
    age (возраст сотрудника)
Метод:
    introduce() — метод, с помощью которого сотрудник может самопредставиться. Метод должен выводить сообщение вида: "Меня зовут {name}, мне {age} лет."


Создайте класс Company:
Атрибут:
    workers (список сотрудников)
Методы:
    add_worker(worker) — метод для добавления нового сотрудника в список компании.
    find_worker(worker_name) — метод для поиска сотрудника по имени.
    fire_worker(worker_name) — метод для увольнения сотрудника по имени.
"""
