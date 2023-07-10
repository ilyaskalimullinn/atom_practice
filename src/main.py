import traceback

from apps import app
from base import error_view
from config import DEBUG
from exceptions import ServiceException

if __name__ == '__main__':
    try:
        app()
    except ServiceException as e:
        error_view.print_error(e)
    except Exception as e:
        if DEBUG:
            traceback.print_exception(e)
        else:
            error_view.print_error("Unknown error")
