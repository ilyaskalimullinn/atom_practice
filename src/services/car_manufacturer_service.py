from typing import List

from db.models import CarManufacturer
from db.repositories import ICarManufacturerRepository
from exceptions import DbNotFoundException, ServiceException
from serializers import CarManufacturerSerializer


class CarManufacturerService:
    car_manufacturer_repository: ICarManufacturerRepository

    def __init__(self, car_manufacturer_repository: ICarManufacturerRepository) -> None:
        self.car_manufacturer_repository = car_manufacturer_repository

    def find_all(self) -> List[CarManufacturer]:
        return self.car_manufacturer_repository.find_all()

    def create(self, serializer: CarManufacturerSerializer) -> CarManufacturer:
        if not serializer.is_valid():
            raise ServiceException("Validation exception")
        manufacturer = serializer.to_obj()
        self.car_manufacturer_repository.save(manufacturer)
        return manufacturer

    def delete(self, id: int) -> CarManufacturer:
        car_manufacturer = self.car_manufacturer_repository.find_by_id(id)
        if car_manufacturer is None:
            raise ServiceException(f"No car manufacturer with id {id}")
        self.car_manufacturer_repository.delete(car_manufacturer)
        return car_manufacturer

    def update(self, serializer: CarManufacturerSerializer) -> CarManufacturer:
        if not serializer.is_valid():
            raise ServiceException("Validation exception")
        if serializer.id is None:
            raise ServiceException("Invalid car manufacturer id")
        manufacturer = serializer.to_obj()
        self.car_manufacturer_repository.save(manufacturer)
        return manufacturer
