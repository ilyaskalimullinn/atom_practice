from typing import List

from db.models import CarModel
from db.repositories import CarModelRepository
from serializers import CarModelSerializer


class CarModelService:
    car_model_repository: CarModelRepository

    def __init__(self, car_model_repository: CarModelRepository) -> None:
        self.car_model_repository = car_model_repository

    def find_all(self) -> List[CarModel]:
        return self.car_model_repository.find_all_join_manufacturer()

    def create(self, serializer: CarModelSerializer) -> CarModel:
        if not serializer.is_valid():
            raise ValueError("Validation error")
        car_model = serializer.to_obj()
        self.car_model_repository.save(car_model)
        return car_model
