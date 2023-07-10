from typing import Type

from db.models import Car
from db.repositories import IModelCrudRepository
from services import BaseCrudService, T


class CarService(BaseCrudService[Car]):

    def __init__(self, model_repository: IModelCrudRepository[T]) -> None:
        super().__init__(model_repository, Car)
