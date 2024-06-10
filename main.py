# Простой класс для представления книги
class Book:
    def init(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year

    def display_info(self):
        print(f"Книга: {self.title}")
        print(f"Автор: {self.author}")
        print(f"Год выпуска: {self.year}")

# Создание экземпляра книги
my_book = Book("Война и мир", "Лев Толстой", 1869)

# Вывод информации о книге
my_book.display_info()