from __future__ import annotations

from abc import ABC, abstractmethod


class Vehicle(ABC):
    """Базовий абстрактний клас транспортного засобу."""

    @abstractmethod
    def start_engine(self) -> None:
        """Запустити двигун транспортного засобу."""
        raise NotImplementedError
