from __future__ import annotations

from abc import ABC, abstractmethod

from .base import Vehicle
from .concrete import Car, Motorcycle


class VehicleFactory(ABC):
    """Абстрактна фабрика для створення транспортних засобів."""

    @abstractmethod
    def create_car(self, make: str, model: str) -> Vehicle:
        raise NotImplementedError

    @abstractmethod
    def create_motorcycle(self, make: str, model: str) -> Vehicle:
        raise NotImplementedError


class USVehicleFactory(VehicleFactory):
    """Фабрика для ринку США (US Spec)."""

    REGION = "US Spec"

    def create_car(self, make: str, model: str) -> Vehicle:
        return Car(make=make, model=model, region_spec=self.REGION)

    def create_motorcycle(self, make: str, model: str) -> Vehicle:
        return Motorcycle(make=make, model=model, region_spec=self.REGION)


class EUVehicleFactory(VehicleFactory):
    """Фабрика для ринку ЄС (EU Spec)."""

    REGION = "EU Spec"

    def create_car(self, make: str, model: str) -> Vehicle:
        return Car(make=make, model=model, region_spec=self.REGION)

    def create_motorcycle(self, make: str, model: str) -> Vehicle:
        return Motorcycle(make=make, model=model, region_spec=self.REGION)
