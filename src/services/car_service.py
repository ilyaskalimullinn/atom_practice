from typing import List

from db.models import Car
from db.repositories import ICarRepository


class CarService:
    car_repository: ICarRepository

    def __init__(self, car_repository: ICarRepository) -> None:
        self.car_repository = car_repository

    def find_all(self) -> List[Car]:
        return self.car_repository.find_all()
