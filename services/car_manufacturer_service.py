from typing import List

from db.models import CarManufacturer
from db.repositories import CarManufacturerRepository
from serializers import CarManufacturerSerializer


class CarManufacturerService:
    car_manufacturer_repository: CarManufacturerRepository

    def __init__(self, car_manufacturer_repository: CarManufacturerRepository) -> None:
        self.car_manufacturer_repository = car_manufacturer_repository

    def find_all(self) -> List[CarManufacturer]:
        return self.car_manufacturer_repository.find_all()

    def create(self, serializer: CarManufacturerSerializer) -> CarManufacturer:
        if not serializer.is_valid():
            raise ValueError("Validation exception")
        manufacturer = serializer.to_obj()
        self.car_manufacturer_repository.create(manufacturer)
        return manufacturer
