import abc
from typing import List

from sqlalchemy.orm import joinedload

from db.db import Session
from db.models import CarManufacturer, CarModel


class ICarManufacturerRepository(abc.ABC):
    @abc.abstractmethod
    def find_all(self) -> List[CarManufacturer]:
        pass

    @abc.abstractmethod
    def save(self, manufacturer: CarManufacturer) -> None:
        pass


class ICarModelRepository(abc.ABC):
    @abc.abstractmethod
    def find_all(self) -> List[CarModel]:
        pass

    @abc.abstractmethod
    def save(self, model: CarModel) -> None:
        pass


class CarManufacturerRepository(ICarManufacturerRepository):
    session: Session

    def __init__(self, session: Session) -> None:
        self.session = session

    def find_all(self) -> List[CarManufacturer]:
        return self.session.query(CarManufacturer).all()

    def save(self, manufacturer: CarManufacturer) -> None:
        self.session.add(manufacturer)
        self.session.commit()


class CarModelRepository(ICarModelRepository):
    session: Session

    def __init__(self, session: Session) -> None:
        self.session = session

    def find_all(self) -> List[CarModel]:
        return self.session.query(CarModel).options(joinedload(CarModel.manufacturer)).all()

    def save(self, car_model: CarModel) -> None:
        self.session.add(car_model)
        self.session.commit()
