from db.models import CarUsage
from db.repositories import ICarUsageRepository
from services import BaseCrudService


class CarUsageService(BaseCrudService[CarUsage]):
    def __init__(self, model_repository: ICarUsageRepository) -> None:
        super().__init__(model_repository, CarUsage)
