from __future__ import annotations

import logging

# Налаштовуємо базове логування
logging.basicConfig(level=logging.INFO, format="%(message)s")


class Book:
    """Клас, що зберігає інформацію про книгу."""

    def __init__(self, title: str, author: str, year: str) -> None:
        # Назва книги
        self.title = title
        # Автор книги
        self.author = author
        # Рік видання
        self.year = year

    def __str__(self) -> str:
        """Повертає рядкове представлення книги."""
        return f"Title: {self.title}, Author: {self.author}, Year: {self.year}"


if __name__ == "__main__":
    # Невеликий самотест для перевірки
    example = Book("The Pragmatic Programmer", "Andrew Hunt", "1999")
    logging.info(example)
