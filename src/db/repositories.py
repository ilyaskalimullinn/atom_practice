import abc
from typing import List, Optional

from sqlalchemy.orm import joinedload

from db.db import Session
from db.models import CarManufacturer, CarModel
from exceptions import DbNotFoundException


class ICarManufacturerRepository(abc.ABC):
    @abc.abstractmethod
    def find_all(self) -> List[CarManufacturer]:
        pass

    @abc.abstractmethod
    def find_by_id(self, id: int) -> Optional[CarManufacturer]:
        pass

    @abc.abstractmethod
    def save(self, manufacturer: CarManufacturer) -> None:
        pass

    @abc.abstractmethod
    def delete(self, car_manufacturer: CarManufacturer) -> CarManufacturer:
        pass


class ICarModelRepository(abc.ABC):
    @abc.abstractmethod
    def find_all(self) -> List[CarModel]:
        pass

    @abc.abstractmethod
    def find_by_id(self, id: int) -> Optional[CarModel]:
        pass

    @abc.abstractmethod
    def save(self, model: CarModel) -> None:
        pass

    @abc.abstractmethod
    def delete(self, model: CarModel) -> None:
        pass


class CarManufacturerRepository(ICarManufacturerRepository):

    session: Session

    def __init__(self, session: Session) -> None:
        self.session = session

    def find_all(self) -> List[CarManufacturer]:
        return self.session.query(CarManufacturer).all()

    def save(self, manufacturer: CarManufacturer) -> None:
        if manufacturer.id is None:
            self.session.add(manufacturer)
        else:
            self.session.merge(manufacturer)
        self.session.commit()

    def find_by_id(self, id: int) -> Optional[CarManufacturer]:
        return self.session.get(CarManufacturer, id)

    def delete(self, car_manufacturer: CarManufacturer) -> None:
        self.session.delete(car_manufacturer)
        self.session.commit()


class CarModelRepository(ICarModelRepository):
    session: Session

    def __init__(self, session: Session) -> None:
        self.session = session

    def find_all(self) -> List[CarModel]:
        return self.session.query(CarModel).options(joinedload(CarModel.manufacturer)).all()

    def save(self, car_model: CarModel) -> None:
        if car_model.id is None:
            self.session.add(car_model)
        else:
            self.session.merge(car_model)
        self.session.commit()

    def find_by_id(self, id: int) -> Optional[CarModel]:
        return self.session.get(CarModel, id)

    def delete(self, model: CarModel) -> None:
        self.session.delete(model)
        self.session.commit()


