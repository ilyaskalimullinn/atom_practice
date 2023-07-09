import rich
import typer
from rich.prompt import Prompt

from db.repositories import CarManufacturerRepository
from serializers import CarManufacturerSerializer
from services.car_manufacturer_service import CarManufacturerService
from base import session, console
from views.car_manufacturer_view import CarManufacturerView

car_manufacturer_app = typer.Typer()
car_manufacturer_repository = CarManufacturerRepository(session)
car_manufacturer_service = CarManufacturerService(car_manufacturer_repository)
car_manufacturer_view = CarManufacturerView(console=console)


@car_manufacturer_app.command("ls")
def find_all():
    """Get a list of all car manufacturers"""
    lst = car_manufacturer_service.find_all()
    car_manufacturer_view.print(lst)


@car_manufacturer_app.command("create")
def create_prompt():
    """Add a new car manufacturer using prompt"""
    serializer = CarManufacturerSerializer()
    serializer.name = Prompt.ask("Manufacturer name")
    manufacturer = car_manufacturer_service.create(serializer)
    car_manufacturer_view.print(manufacturer)
