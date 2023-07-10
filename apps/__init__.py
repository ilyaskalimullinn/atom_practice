import typer

from apps.car_manufacturer_app import car_manufacturer_app
from apps.car_model_app import car_model_app

app = typer.Typer()
app.add_typer(car_manufacturer_app, name='manufacturer')
app.add_typer(car_model_app, name='model')
