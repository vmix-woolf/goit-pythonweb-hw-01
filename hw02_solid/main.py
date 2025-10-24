from __future__ import annotations

import logging

from hw02_solid.interfaces import LibraryInterface
from hw02_solid.library import UniqueTitleLibrary
from hw02_solid.manager import LibraryManager

# Налаштування базового логування
logging.basicConfig(level=logging.INFO, format="%(message)s")


def main() -> None:
    """Точка входу до застосунку."""

    # Можемо обрати реалізацію бібліотеки (звичайну або з унікальними назвами)
    library: LibraryInterface = UniqueTitleLibrary()

    # Менеджер залежить від абстракції, а не реалізації (DIP)
    manager = LibraryManager(library)

    while True:
        command = input("Enter command (add, remove, show, exit): ").strip().lower()

        match command:
            case "add":
                title = input("Enter book title: ").strip()
                author = input("Enter book author: ").strip()
                try:
                    year = int(input("Enter book year: ").strip())
                except ValueError:
                    logging.info("Рік має бути числом!")
                    continue
                manager.add_book(title, author, year)
            case "remove":
                title = input("Enter book title to remove: ").strip()
                manager.remove_book(title)
            case "show":
                manager.show_books()
            case "exit":
                break
            case _:
                logging.info("Invalid command. Please try again.")


if __name__ == "__main__":
    main()
