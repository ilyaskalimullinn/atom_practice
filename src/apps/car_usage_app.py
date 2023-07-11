import typer
from rich.prompt import Prompt, Confirm

from base import car_usage_service, car_usage_view
from serializers import CarUsageSerializer

car_usage_app = typer.Typer(help="Service to access and manipulate info about car usages: Taxi, Carsharing etc.")


@car_usage_app.command("ls")
def find_all():
    """Get a list of all car usages"""
    lst = car_usage_service.find_all()
    car_usage_view.print_table(*lst)


@car_usage_app.command("create")
def create_prompt():
    """Add a new car usage using prompt"""
    serializer = CarUsageSerializer()
    serializer.name = Prompt.ask("Car usage name")
    manufacturer = car_usage_service.create(serializer)
    car_usage_view.created(manufacturer)


@car_usage_app.command("delete")
def delete(id: int):
    """Delete car usage by id"""
    is_confirmed = Confirm.ask(f"Are you sure you want to delete car usage with id {id}?")
    if is_confirmed:
        usage = car_usage_service.delete_by_id(id)
        car_usage_view.deleted(usage)


@car_usage_app.command("update")
def update_prompt(id: int):
    """Update car usage info using prompt"""
    serializer = CarUsageSerializer()
    serializer.id = id
    serializer.name = Prompt.ask("New name")
    manufacturer = car_usage_service.update(serializer)
    car_usage_view.updated(manufacturer)

