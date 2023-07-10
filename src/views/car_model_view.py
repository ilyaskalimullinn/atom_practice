from typing import Union, List

from rich.console import Console
from rich.table import Table

from db.models import CarModel


class CarModelView:
    console: Console

    def __init__(self, console: Console) -> None:
        self.console = console

    def print(self, models: Union[List[CarModel], CarModel]) -> None:
        if type(models) == CarModel:
            models = [models]
        table = Table("id", "name", "release_date", "manufacturer")
        for m in models:
            table.add_row(str(m.id), m.name, str(m.release_date), m.manufacturer.name)
        self.console.print(table)

    def deleted(self, model: CarModel):
        self.console.print(f"Successfully deleted car model {model.name}, id {model.id}")
