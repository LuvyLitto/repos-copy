class Book:
    def init(self, title, author):
        self.title = title
        self.author = author

    def display_info(self):
        print(f"Книга: {self.title}")
        print(f"Автор: {self.author}")

# Создание экземпляра книги
my_book = Book("Война и мир", "Лев Толстой")

# Вывод информации о книге
my_book.display_info()