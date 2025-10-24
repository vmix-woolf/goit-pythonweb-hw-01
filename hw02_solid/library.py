from __future__ import annotations

import logging

from hw02_solid.interfaces import LibraryInterface
from hw02_solid.models import Book

# Увімкнемо базове логування INFO (замість print)
logging.basicConfig(level=logging.INFO, format="%(message)s")


class Library(LibraryInterface):
    """Базова реалізація бібліотеки.
    Відповідає інтерфейсу LibraryInterface (LSP)
    і може розширюватись без зміни коду (OCP).
    """

    def __init__(self) -> None:
        # Сховище книг (тільки об'єкти Book)
        self._books: list[Book] = []

    def add_book(self, book: Book) -> None:
        """Додати книгу до бібліотеки."""
        self._books.append(book)
        logging.info("Книгу '%s' додано.", book.title)

    def remove_book(self, title: str) -> None:
        """Видалити книгу за назвою (якщо знайдено)."""
        for idx, b in enumerate(self._books):
            if b.title == title:
                del self._books[idx]
                logging.info("Книгу '%s' видалено.", title)
                return
        logging.info("Книгу '%s' не знайдено.", title)

    def get_books(self) -> list[Book]:
        """Повернути копію списку книг (інкапсуляція)."""
        return list(self._books)


# ↓ Приклад розширення (OCP) зі збереженням підстановлюваності (LSP)
class UniqueTitleLibrary(Library):
    """Розширення: не дозволяє дублікати назв."""

    def add_book(self, book: Book) -> None:
        # Перевірка на наявність книги з такою ж назвою
        if any(b.title == book.title for b in self.get_books()):
            logging.info("Книгу з назвою '%s' вже додано.", book.title)
            return
        super().add_book(book)
