from typing import List

from db.models import CarModel
from db.repositories import ICarModelRepository
from serializers import CarModelSerializer


class CarModelService:
    car_model_repository: ICarModelRepository

    def __init__(self, car_model_repository: ICarModelRepository) -> None:
        self.car_model_repository = car_model_repository

    def find_all(self) -> List[CarModel]:
        return self.car_model_repository.find_all()

    def create(self, serializer: CarModelSerializer) -> CarModel:
        if not serializer.is_valid():
            raise ValueError("Validation error")
        car_model = serializer.to_obj()
        self.car_model_repository.save(car_model)
        return car_model
