import typer

from base import car_service, car_view

car_app = typer.Typer()


@car_app.command("ls")
def find_all():
    """Get a list of all cars"""
    lst = car_service.find_all()
    car_view.print_table(*lst)
