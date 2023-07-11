from typing import Optional

from db.models import CarModel
from db.repositories import ICarModelRepository
from services import BaseCrudService, T


class CarModelService(BaseCrudService[CarModel]):

    def __init__(self, model_repository: ICarModelRepository) -> None:
        super().__init__(model_repository, CarModel)
        self.model_repository: ICarModelRepository = model_repository

    def find_by_name(self, model_name: str, manufacturer_name: str) -> Optional[T]:
        return self.model_repository.find_by_name(model_name=model_name, manufacturer_name=manufacturer_name)
