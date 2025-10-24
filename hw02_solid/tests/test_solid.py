from __future__ import annotations

from collections.abc import Generator

import pytest

from hw02_solid.library import Library
from hw02_solid.manager import LibraryManager


@pytest.fixture()  # type: ignore[misc]
def setup_library() -> Generator[LibraryManager, None, None]:
    """Створює менеджер бібліотеки для тестів."""
    lib = Library()
    manager = LibraryManager(lib)
    yield manager


def test_add_and_show_books(
    setup_library: LibraryManager, caplog: pytest.LogCaptureFixture
) -> None:
    """Перевіряє додавання та відображення книг."""
    caplog.set_level("INFO")
    manager = setup_library
    manager.add_book("Clean Code", "Robert C. Martin", 2008)
    manager.show_books()

    assert "Clean Code" in caplog.text
    assert "Robert C. Martin" in caplog.text


def test_remove_book(
    setup_library: LibraryManager, caplog: pytest.LogCaptureFixture
) -> None:
    """Перевіряє видалення книги."""
    caplog.set_level("INFO")
    manager = setup_library
    manager.add_book("Refactoring", "Martin Fowler", 1999)
    manager.remove_book("Refactoring")

    assert "видалено" in caplog.text
