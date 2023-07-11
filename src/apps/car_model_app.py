import datetime

import typer
from rich.prompt import Prompt, Confirm

from base import car_model_service, car_model_view, car_manufacturer_service
from serializers import CarModelSerializer

car_model_app = typer.Typer(help="Service to access and manipulate info about car models")


@car_model_app.command("ls")
def find_all():
    """Get all car models in system"""
    res = car_model_service.find_all()
    car_model_view.print_table(*res)


@car_model_app.command("create")
def create_prompt():
    """Create car model using prompt"""
    serializer = prompt_car_model()

    car_model = car_model_service.create(serializer)
    car_model_view.print_table(car_model)


@car_model_app.command("delete")
def delete(id: int):
    """Delete car model by id"""
    is_confirmed = Confirm.ask(f"Are you sure you want to delete car model with id {id}?")
    if is_confirmed:
        model = car_model_service.delete_by_id(id)
        car_model_view.deleted(model)


@car_model_app.command("update")
def update_prompt(id: int):
    """Update car model info by id"""
    serializer = prompt_car_model()
    serializer.id = id
    car_model = car_model_service.update(serializer)
    car_model_view.updated(car_model)


def prompt_car_model() -> CarModelSerializer:
    date_format = "%d-%m-%Y"
    serializer = CarModelSerializer()
    serializer.name = Prompt.ask("name")
    serializer.release_date = datetime.datetime.strptime(Prompt.ask("release date, format dd-MM-yyyy"),
                                                         date_format).date()

    manufacturer_list = car_manufacturer_service.find_all()
    manufacturer_name = Prompt.ask("manufacturer", choices=[m.name for m in manufacturer_list])
    serializer.manufacturer_id = list(filter(lambda x: x.name == manufacturer_name, manufacturer_list))[0].id
    serializer.base_price = int(Prompt.ask("Base price, rubles"))
    return serializer
