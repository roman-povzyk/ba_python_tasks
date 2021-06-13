# Write a class structure that implements a library. Classes:
# 1) Library - name, books = [], authors = []
# 2) Book - name, year, author (author must be an instance of Author class)
# 3) Author - name, country, birthday, books = []

# Library class
# Methods:
# - new_book(name: str, year: int, author: Author) - returns an instance of Book class
# and adds the book to the books list for the current library.
# - group_by_author(author: Author) - returns a list of all books grouped by the specified author
# - group_by_year(year: int) - returns a list of all the books grouped by the specified year
# All 3 classes must have a readable __repr__ and __str__ methods.
# Also, the book class should have a class variable which holds the amount of all existing books

class Author:
    author_total_numbers = 0

    def __init__(self, name, country, birthday, books):
        """створюємо клас для автора"""
        self.name = name
        self.country = country
        self.birthday = birthday
        self.books = books
        Author.author_total_numbers += 1


class Book(Author):
    book_total_numbers = 0

    def __init__(self, name, year, author):
        """створюємо клас для книги"""
        self.name = name
        self.year = year
        self.author = author
        # тут рахуватимемо загальну кількість книг у бібліотеці
        Book.book_total_numbers += 1


class Library(Book):
    def __init__(self, name):
        """створюємо клас для бібліотеки"""
        self.name = name
        self.all_books = []

    def new_book(self, book):
        """метод для прийняття книг у бібліотеку"""
        # перевіряємо чи коректно введений рік видання
        if not str(book.year).isdigit():
            print('На жаль, книга має некоректно введений рік. Тому її рік буде — «0000»')
            book.year = '0000'
        # додаємо книгу у бібліотеку
        self.all_books.append({'name': book.name, 'year': book.year, 'author': book.author.name})

    def group_by_author(self, author):
        """метод для групування за автором"""
        book_count = 0
        print(f'Всі книги за запитом «{author.name}», які є у нашій бібліотеці: ')
        for book in self.all_books:
            if author.name == book['author']:
                book_count += 1
                print(f"№{book_count}: «{book['name']}» ({book['year']} рік)")
        if book_count == 0:
            print(f'На жаль, за запитом «{author.name}» {self.name} немає жодної книги.')

    def group_by_year(self, year):
        """метод для групування за роком"""
        book_count = 0
        print(f'Всі книги, які вийшли {year} року і є у нашій бібліотеці: ')
        for book in self.all_books:
            if year == book['year']:
                book_count += 1
                print(f"№{book_count}: «{book['name']}», автор — {book['author']}")
        if book_count == 0:
            print(f'На жаль, {self.name} немає жодної книги, яка вийшла у {year} році.')


# створюємо нашу бібліотеку
our_library = Library('Полтавська обласна універсальна наукова бібліотека ім. І.П. Котляревського')

# вводимо чотирьох авторів
author_1 = Author('Стівен Кінг', 'США', '21.09.1947', [])
author_2 = Author('Алан Дін Фостер', 'США', '18.11.1946', [])
author_3 = Author('Дуглас Адамс', 'Велика Британія', '11.03.1952', [])
author_4 = Author('Максим Кідрук', 'Україна', '01.04.1984', [])

# створюємо базу книг цих авторів
book_1 = Book('Доктор Сон', '2013', author_1)
book_2 = Book('Зелена миля', '1996', author_1)
book_3 = Book('Історія Лізі', '2006', author_1)
book_4 = Book('11/22/63', '2011', author_1)
book_5 = Book('Чужий', '1979', author_2)
book_6 = Book('Чужі', '1986', author_2)
book_7 = Book('Чужий 3', '1992', author_2)
book_8 = Book('Путівник Галактикою для космотуристів', '1979', author_3)
book_9 = Book('Ресторан «На Краю Всесвіту»', '1980', author_3)
book_10 = Book('Життя, Всесвіт і все інше', '1982', author_3)
book_11 = Book('Путівник Галактикою для космотуристів', 'сорок два', author_3)

# додаємо до бібліотеки ці книги
our_library.new_book(book_1)
our_library.new_book(book_2)
our_library.new_book(book_3)
our_library.new_book(book_4)
our_library.new_book(book_5)
our_library.new_book(book_6)
our_library.new_book(book_7)
our_library.new_book(book_8)
our_library.new_book(book_9)
our_library.new_book(book_10)
our_library.new_book(book_11)

# групуємо книги за нашими авторами
our_library.group_by_author(author_1)
our_library.group_by_author(author_2)
our_library.group_by_author(author_3)
our_library.group_by_author(author_4)

# групуємо книги за роками
our_library.group_by_year('1979')
our_library.group_by_year('2021')

# отримуємо кількість книг, яку має бібліотека
print(f'К-ть книг у бібліотеці: {Book.book_total_numbers} шт. '
      f'К-ть авторів: {Author.author_total_numbers}.')
