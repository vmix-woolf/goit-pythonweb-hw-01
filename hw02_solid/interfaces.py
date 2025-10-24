from __future__ import annotations

from abc import ABC, abstractmethod

from hw02_solid.models import Book


class LibraryInterface(ABC):
    """Інтерфейс, який визначає контракт для бібліотеки."""

    @abstractmethod
    def add_book(self, book: Book) -> None:
        """Додає книгу до бібліотеки."""
        pass

    @abstractmethod
    def remove_book(self, title: str) -> None:
        """Видаляє книгу за назвою."""
        pass

    @abstractmethod
    def get_books(self) -> list[Book]:
        """Повертає список усіх книг."""
        pass
