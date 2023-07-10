from rich.console import Console

from db.db import Session
from db.repositories import CarManufacturerRepository, CarModelRepository, CarUsageRepository
from services.car_manufacturer_service import CarManufacturerService
from services.car_model_service import CarModelService
from services.car_usage_service import CarUsageService
from views.car_manufacturer_view import CarManufacturerView
from views.car_model_view import CarModelView
from views.car_usage_view import CarUsageView
from views.error_view import ErrorView

session = Session()
console = Console()

error_view = ErrorView(console)

car_manufacturer_repository = CarManufacturerRepository(session)
car_manufacturer_service = CarManufacturerService(car_manufacturer_repository)
car_manufacturer_view = CarManufacturerView(console=console)

car_model_repository = CarModelRepository(session)
car_model_service = CarModelService(car_model_repository)
car_model_view = CarModelView(console)

car_usage_repository = CarUsageRepository(session)
car_usage_service = CarUsageService(car_usage_repository)
car_usage_view = CarUsageView(console)
