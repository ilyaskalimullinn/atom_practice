from typing import List, Union

from rich.console import Console
from rich.table import Table

from db.models import CarManufacturer


class CarManufacturerView:
    console: Console

    def __init__(self, console: Console) -> None:
        self.console = console

    def print(self, manufacturers: Union[List[CarManufacturer], CarManufacturer]):
        if type(manufacturers) == CarManufacturer:
            manufacturers = [manufacturers]
        table = Table("id", "name")
        for m in manufacturers:
            table.add_row(str(m.id), m.name)
        self.console.print(table)
