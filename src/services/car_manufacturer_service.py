from db.models import CarManufacturer
from db.repositories import ICarManufacturerRepository
from services import BaseCrudService


class CarManufacturerService(BaseCrudService[CarManufacturer]):
    def __init__(self, car_manufacturer_repository: ICarManufacturerRepository) -> None:
        super().__init__(car_manufacturer_repository, CarManufacturer)
