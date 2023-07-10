import typer

from apps.car_manufacturer_app import car_manufacturer_app
from apps.car_model_app import car_model_app
from db.db import create_all_tables

app = typer.Typer()
app.add_typer(car_manufacturer_app, name='manufacturer')
app.add_typer(car_model_app, name='model')


@app.command("init_db")
def init_db():
    """Initialize database, create tables"""
    create_all_tables()
