import typer

from apps.car_manufacturer_app import car_manufacturer_app

app = typer.Typer()
app.add_typer(car_manufacturer_app, name='manufacturer')
