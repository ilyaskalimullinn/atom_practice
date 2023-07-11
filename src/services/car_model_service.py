from db.models import CarModel
from db.repositories import ICarModelRepository
from services import BaseCrudService, T


class CarModelService(BaseCrudService[CarModel]):

    def __init__(self, model_repository: ICarModelRepository) -> None:
        super().__init__(model_repository, CarModel)
