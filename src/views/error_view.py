from typing import Union

from rich.console import Console


class ErrorView:
    console: Console

    def __init__(self, console: Console) -> None:
        self.console = console

    def print_error(self, e: Union[Exception, str]):
        e = str(e)
        self.console.print(e, style="red on white")
