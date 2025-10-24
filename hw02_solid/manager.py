from __future__ import annotations

import logging

from hw02_solid.interfaces import LibraryInterface
from hw02_solid.models import Book


class LibraryManager:
    """Керує взаємодією користувача з бібліотекою.
    Використовує абстракцію LibraryInterface (DIP).
    """

    def __init__(self, library: LibraryInterface) -> None:
        self._library = library

    def add_book(self, title: str, author: str, year: int) -> None:
        """Додає книгу до бібліотеки."""
        book = Book(title, author, year)
        self._library.add_book(book)
        logging.info("Додано книгу: %s (%s, %s)", book.title, book.author, book.year)

    def remove_book(self, title: str) -> None:
        """Видаляє книгу з бібліотеки за назвою."""
        self._library.remove_book(title)

    def show_books(self) -> None:
        """Виводить усі книги бібліотеки."""
        books = self._library.get_books()
        if not books:
            logging.info("Бібліотека порожня.")
            return

        for book in books:
            logging.info(
                "Назва: %s | Автор: %s | Рік: %s",
                book.title,
                book.author,
                book.year,
            )
