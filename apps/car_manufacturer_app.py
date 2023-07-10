import typer
from rich.prompt import Prompt

from base import car_manufacturer_service, car_manufacturer_view
from serializers import CarManufacturerSerializer

car_manufacturer_app = typer.Typer()


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
