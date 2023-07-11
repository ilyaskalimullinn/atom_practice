import typer

from base import can_data_reader_service

car_dbc_app = typer.Typer(help="Simple service that provides a way to read raw CAN data")


@car_dbc_app.command("read")
def read(dbc_path: str, data_path: str) -> None:
    results = can_data_reader_service.decode_data(dbc_path, data_path)
    for result in results:
        print(result)
