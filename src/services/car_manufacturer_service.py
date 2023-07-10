from typing import List

from db.models import CarManufacturer
from db.repositories import ICarManufacturerRepository
from exceptions import DbNotFoundException, ServiceException
from serializers import CarManufacturerSerializer
from services import BaseCrudService


class CarManufacturerService(BaseCrudService):
    def __init__(self, car_manufacturer_repository: ICarManufacturerRepository) -> None:
        super().__init__(car_manufacturer_repository, CarManufacturer)
