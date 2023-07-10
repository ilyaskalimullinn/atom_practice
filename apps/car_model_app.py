import datetime
from datetime import date

import typer
from rich.prompt import Prompt

from base import car_model_service, car_model_view, car_manufacturer_service
from serializers import CarModelSerializer

car_model_app = typer.Typer()


@car_model_app.command("ls")
def find_all():
    res = car_model_service.find_all()
    car_model_view.print(res)


@car_model_app.command("create")
def create_prompt():
    date_format = "%d-%m-%Y"
    serializer = CarModelSerializer()
    serializer.name = Prompt.ask("name")
    serializer.release_date = datetime.datetime.strptime(Prompt.ask("release date, format dd-MM-yyyy"), date_format).date()

    manufacturer_list = car_manufacturer_service.find_all()
    manufacturer_name = Prompt.ask("manufacturer", choices=[m.name for m in manufacturer_list])
    serializer.manufacturer_id = list(filter(lambda x: x.name == manufacturer_name, manufacturer_list))[0].id

    car_model = car_model_service.create(serializer)
    car_model_view.print(car_model)
