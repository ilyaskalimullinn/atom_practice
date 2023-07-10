from apps import app
from base import error_view
from exceptions import ServiceException

if __name__ == '__main__':
    try:
        app()
    except ServiceException as e:
        error_view.print_error(e)
    except Exception:
        error_view.print_error("Unknown error")
