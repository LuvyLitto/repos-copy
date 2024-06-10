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
my_book1 = Book("Война и мир", "Лев Толстой", 1869)
my_book2 = Book("1984", "Джордж Оруэлл", 1949, "дистопия")

my_book1.display_info()
my_book2.display_info()