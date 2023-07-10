from typing import List, Union

from rich.console import Console
from rich.table import Table

from db.models import CarManufacturer
from views import GenericModelView


class CarManufacturerView(GenericModelView[CarManufacturer]):
    def __init__(self, console: Console) -> None:
        super().__init__(console, table_columns=["id", "name"], table_column_labels=["Id", "Name"])

