from __future__ import annotations

import logging
from dataclasses import dataclass

from .base import Vehicle


@dataclass(slots=True)
class Car(Vehicle):
    """Клас автомобіля з регіональною специфікацією."""

    make: str
    model: str
    region_spec: str

    def start_engine(self) -> None:
        logging.info(
            "%s %s (%s): Двигун запущено", self.make, self.model, self.region_spec
        )


@dataclass(slots=True)
class Motorcycle(Vehicle):
    """Клас мотоцикла з регіональною специфікацією."""

    make: str
    model: str
    region_spec: str

    def start_engine(self) -> None:
        logging.info(
            "%s %s (%s): Мотор заведено", self.make, self.model, self.region_spec
        )
