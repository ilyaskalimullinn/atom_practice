from datetime import datetime

import typer
from rich.prompt import Prompt, Confirm

from base import car_service, car_view, car_model_service, car_usage_service
from serializers import CarSerializer

car_app = typer.Typer()


@car_app.command("ls")
def find_all():
    """Get a list of all cars"""
    lst = car_service.find_all()
    car_view.print_table(*lst)


@car_app.command("create")
def create_prompt():
    """Create car using prompt"""
    serializer = prompt_car()

    car_model = car_service.create(serializer)
    car_view.print_table(car_model)


@car_app.command("update")
def update_prompt(id: int):
    """Update car info by id using prompt"""
    serializer = prompt_car()
    serializer.id = id
    car_model = car_service.update(serializer)
    car_view.updated(car_model)


@car_app.command("delete")
def delete(id: int):
    """Delete car by id"""
    is_confirmed = Confirm.ask(f"Are you sure you want to delete car with id {id}?")
    if is_confirmed:
        model = car_service.delete_by_id(id)
        car_view.deleted(model)


def prompt_car() -> CarSerializer:
    date_format = "%d-%m-%Y"
    serializer = CarSerializer()

    model_prompt = Prompt.ask("Do you want to enter car model id or its name?", choices=["id", "name"])
    if model_prompt == "id":
        serializer.model_id = int(Prompt.ask("Car model id"))
    else:
        manufacturer_name = Prompt.ask("Car model manufacturer")
        model_name = Prompt.ask("Car model name")
        model = car_model_service.find_by_name(model_name=model_name, manufacturer_name=manufacturer_name)
        serializer.model_id = model.id

    serializer.plate_number = Prompt.ask("Plate number")
    serializer.manufacture_date = datetime.strptime(Prompt.ask("Date of manufacture, format dd-MM-yyyy"),
                                                date_format).date()
    serializer.mileage = int(Prompt.ask("Mileage, km"))

    all_usages = car_usage_service.find_all()
    usage_name = Prompt.ask("Car usage", choices=[u.name for u in all_usages])
    if usage_name != "":
        usage = list(filter(lambda u: u.name == usage_name, all_usages))[0]
        serializer.usage_id = usage.id

    return serializer
