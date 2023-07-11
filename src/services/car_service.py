from typing import Type, Optional

from db.models import Car
from db.repositories import ICarRepository
from services import BaseCrudService, T


class CarService(BaseCrudService[Car]):

    def __init__(self, model_repository: ICarRepository) -> None:
        super().__init__(model_repository, Car)
        self.model_repository: ICarRepository = model_repository

    def find_by_plate_number(self, plate_number: str) -> Optional[Car]:
        return self.model_repository.find_by_plate_number(plate_number)
