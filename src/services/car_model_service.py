from typing import List

from db.models import CarModel
from db.repositories import ICarModelRepository
from exceptions import ServiceException
from serializers import CarModelSerializer


class CarModelService:
    car_model_repository: ICarModelRepository

    def __init__(self, car_model_repository: ICarModelRepository) -> None:
        self.car_model_repository = car_model_repository

    def find_all(self) -> List[CarModel]:
        return self.car_model_repository.find_all()

    def create(self, serializer: CarModelSerializer) -> CarModel:
        if not serializer.is_valid():
            raise ServiceException("Arguments validation error")
        car_model = serializer.to_obj()
        self.car_model_repository.save(car_model)
        return car_model

    def delete(self, id: int) -> CarModel:
        car_model = self.car_model_repository.find_by_id(id)
        if car_model is None:
            raise ServiceException(f"No car model with id {id}")
        self.car_model_repository.delete(car_model)
        return car_model
