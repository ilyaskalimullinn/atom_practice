from typing import List

from db.models import CarUsage
from db.repositories import ICarUsageRepository
from exceptions import ServiceException
from serializers import CarUsageSerializer


class CarUsageService:
    car_usage_repository: ICarUsageRepository

    def __init__(self, car_usage_repository: ICarUsageRepository) -> None:
        self.car_usage_repository = car_usage_repository

    def find_all(self) -> List[CarUsage]:
        return self.car_usage_repository.find_all()

    def create(self, serializer: CarUsageSerializer) -> CarUsage:
        if not serializer.is_valid():
            raise ServiceException("Validation exception")
        usage = serializer.to_obj()
        self.car_usage_repository.save(usage)
        return usage

    def delete(self, id: int) -> CarUsage:
        car_usage = self.car_usage_repository.find_by_id(id)
        if car_usage is None:
            raise ServiceException(f"No car usage with id {id}")
        self.car_usage_repository.delete(car_usage)
        return car_usage

    def update(self, serializer: CarUsageSerializer) -> CarUsage:
        if not serializer.is_valid():
            raise ServiceException("Validation exception")
        if serializer.id is None:
            raise ServiceException("Invalid car usage id")
        usage = serializer.to_obj()
        self.car_usage_repository.save(usage)
        return usage
