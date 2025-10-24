from __future__ import annotations

import logging

from vehicles.factory import EUVehicleFactory, USVehicleFactory


def configure_logging() -> None:
    """Базова конфігурація логування на рівні INFO."""
    logging.basicConfig(
        level=logging.INFO,
        format="%(levelname)s:%(name)s:%(message)s",
    )


def run_demo() -> None:
    """Демонстраційний сценарій створення транспортних засобів через фабрики."""
    us_factory = USVehicleFactory()
    eu_factory = EUVehicleFactory()

    vehicle1 = us_factory.create_car("Ford", "Mustang")
    vehicle2 = eu_factory.create_motorcycle("BMW", "R nineT")

    vehicle1.start_engine()
    vehicle2.start_engine()


if __name__ == "__main__":
    configure_logging()
    run_demo()
