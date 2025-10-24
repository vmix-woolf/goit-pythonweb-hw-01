from __future__ import annotations

import logging
from dataclasses import dataclass

# Налаштовуємо базове логування (єдиний стиль для всієї програми)
logging.basicConfig(level=logging.INFO, format="%(message)s")


@dataclass
class Book:
    """Клас, що зберігає інформацію про книгу."""

    title: str
    author: str
    year: int

    def __str__(self) -> str:
        """Повертає рядкове представлення книги."""
        return f"Title: {self.title}, Author: {self.author}, Year: {self.year}"


if __name__ == "__main__":
    # Невеликий самотест для перевірки
    example = Book("The Pragmatic Programmer", "Andrew Hunt", 1999)
    logging.info(example)
