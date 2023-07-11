import typer

from apps.car_app import car_app
from apps.car_dbc_app import car_dbc_app
from apps.car_manufacturer_app import car_manufacturer_app
from apps.car_model_app import car_model_app
from apps.car_usage_app import car_usage_app
from db.db import create_all_tables

app = typer.Typer()
app.add_typer(car_manufacturer_app, name='manufacturer')
app.add_typer(car_model_app, name='model')
app.add_typer(car_usage_app, name='usage')
app.add_typer(car_app, name="car")
app.add_typer(car_dbc_app, name="dbc")


@app.command("init_db")
def init_db():
    """Initialize database, create tables"""
    create_all_tables()
