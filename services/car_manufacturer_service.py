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
        try:
            return self.car_manufacturer_repository.delete_by_id(id)
        except DbNotFoundException:
            raise ServiceException(f"No car manufacturer with id {id}")
