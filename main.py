# Простой класс для представления книги
class Book:
    def init(self, title, author, year, genre):
        self.title = title
        self.author = author
        self.year = year
        self.genre = genre

    def display_info(self):
        print(f"Книга: {self.title}")
        print(f"Автор: {self.author}")
        print(f"Год выпуска: {self.year}")
        print(f"Жанр: {self.genre}")

# Создание экземпляра книги
my_book = Book("1984", "Джордж Оруэлл", 1949, "дистопия")

# Вывод информации о книге
my_book.display_info())