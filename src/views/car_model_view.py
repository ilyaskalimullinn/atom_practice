from typing import Union, List

from rich.console import Console
from rich.table import Table

from db.models import CarModel
from views import GenericModelView


class CarModelView(GenericModelView):
    def __init__(self, console: Console) -> None:
        special_columns = {
            "manufacturer": lambda model: model.manufacturer.name
        }
        super().__init__(console,
                         table_columns=["id", "name", "release_date", "manufacturer", "base_price"],
                         table_column_labels=["Id", "Name", "Release Date", "Manufacturer", "Base price"],
                         special_columns=special_columns)
