from typing import List, Union

from rich.console import Console
from rich.table import Table

from db.models import CarManufacturer


class CarManufacturerView:
    console: Console

    def __init__(self, console: Console) -> None:
        self.console = console

    def print(self, manufacturers: Union[List[CarManufacturer], CarManufacturer]) -> None:
        if type(manufacturers) == CarManufacturer:
            manufacturers = [manufacturers]
        table = Table("id", "name")
        for m in manufacturers:
            table.add_row(str(m.id), m.name)
        self.console.print(table)

    def print_message(self, message: str) -> None:
        self.console.print(message)

    def deleted(self, manufacturers: Union[CarManufacturer, List[CarManufacturer]]) -> None:
        self.print_message("Successfully deleted manufacturers")
        self.print(manufacturers)

    def created(self, manufacturers: Union[CarManufacturer, List[CarManufacturer]]) -> None:
        self.print_message("Successfully created manufacturers")
        self.print(manufacturers)

    def updated(self, manufacturers: Union[CarManufacturer, List[CarManufacturer]]) -> None:
        self.print_message("Successfully updated manufacturers")
        self.print(manufacturers)
