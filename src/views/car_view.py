from rich.console import Console

from views import GenericModelView, T


class CarView(GenericModelView):
    def __init__(self, console: Console) -> None:
        special_columns = {
            "model": lambda car: f"{car.model.manufacturer.name} {car.model.name}",
            "usage": lambda car: "None" if car.usage is None else car.usage.name,
        }
        super().__init__(console,
                         table_columns=["id", "plate_number", "model", "usage", "mileage", "manufacture_date"],
                         table_column_labels=["Id", "Plate Number", "Car Model", "Usage", "Mileage, km", "Date of manufacture"],
                         special_columns=special_columns)
