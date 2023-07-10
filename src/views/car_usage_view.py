from rich.console import Console

from db.models import CarUsage
from views import GenericModelView, T


class CarUsageView(GenericModelView[CarUsage]):
    def __init__(self, console: Console) -> None:
        super().__init__(console,
                         table_columns=["id", "name"],
                         table_column_labels=["Id", "Name"])
