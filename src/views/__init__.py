from typing import Type, Union, List, TypeVar, Tuple, Optional, Generic, Dict, Callable

from rich.console import Console
from rich.table import Table

T = TypeVar("T")


class GenericModelView(Generic[T]):
    console: Console
    table_columns: List[str]
    table_column_labels: List[str]
    special_columns: Dict[str, Callable[[T], str]]

    def __init__(self,
                 console: Console,
                 table_columns: List[str],
                 table_column_labels: List[str],
                 special_columns: Optional[Dict[str, Callable[[T], str]]] = None) -> None:
        self.console = console
        self.table_columns = table_columns
        self.table_column_labels = table_column_labels
        self.special_columns = {} if special_columns is None else special_columns

        assert len(table_columns) == len(table_column_labels)

    def print_message(self, message: str) -> None:
        self.console.print(message)

    def print_table(self, *objects: T) -> None:
        table = self._create_table(objects)
        self._fill_table(table, objects)
        self.console.print(table)

    def _create_table(self, objects: Tuple[T]) -> Table:
        return Table(*self.table_column_labels)

    def _fill_table(self, table: Table, objects: Tuple[T]) -> None:
        for o in objects:
            row = [self._object_attribute_str(o, column_name) for column_name in self.table_columns]
            table.add_row(*row)

    def _object_attribute_str(self, obj: T, attribute_name: str) -> str:
        if attribute_name in self.special_columns:
            return self.special_columns[attribute_name](obj)
        value = getattr(obj, attribute_name)
        return str(value)

    def print_crud_message(self, operation: str, objects: Optional[Union[T, List[T]]]) -> None:
        self.print_message(f"Successfully {operation}")
        if objects is not None:
            self.print_table(objects)

    def created(self, objects: Optional[Union[T, List[T]]]):
        self.print_crud_message("created", objects)

    def updated(self, objects: Optional[Union[T, List[T]]]):
        self.print_crud_message("updated", objects)

    def deleted(self, objects: Optional[Union[T, List[T]]]):
        self.print_crud_message("deleted", objects)
