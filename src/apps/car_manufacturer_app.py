import typer
from rich.prompt import Prompt, Confirm

from base import car_manufacturer_service, car_manufacturer_view
from serializers import CarManufacturerSerializer

car_manufacturer_app = typer.Typer()


@car_manufacturer_app.command("ls")
def find_all():
    """Get a list of all car manufacturers"""
    lst = car_manufacturer_service.find_all()
    car_manufacturer_view.print_table(*lst)


@car_manufacturer_app.command("create")
def create_prompt():
    """Add a new car manufacturer using prompt"""
    serializer = CarManufacturerSerializer()
    serializer.name = Prompt.ask("Manufacturer name")
    manufacturer = car_manufacturer_service.create(serializer)
    car_manufacturer_view.created(manufacturer)


@car_manufacturer_app.command("delete")
def delete(id: int):
    """Delete car manufacturer by id"""
    is_confirmed = Confirm.ask(f"Are you sure you want to delete manufacturers with id {id}?")
    if is_confirmed:
        manufacturer = car_manufacturer_service.delete_by_id(id)
        car_manufacturer_view.deleted(manufacturer)


@car_manufacturer_app.command("update")
def update_prompt(id: int):
    """Update manufacturer info using prompt"""
    serializer = CarManufacturerSerializer()
    serializer.id = id
    serializer.name = Prompt.ask("New name")
    manufacturer = car_manufacturer_service.update(serializer)
    car_manufacturer_view.updated(manufacturer)
