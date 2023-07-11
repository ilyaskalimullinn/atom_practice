import os
from os.path import dirname, join

import dotenv

SRC_ROOT = dirname(__file__)
PROJECT_ROOT = join(SRC_ROOT, "..")

dotenv.load_dotenv(join(PROJECT_ROOT, ".env"))

DATABASE = {
    "URL": os.environ.get("DB_URL", "postgresql+psycopg2://atom:atom@localhost:5432/atom"),
    "DEBUG": os.environ.get("DB_DEBUG", False).lower() == "true"
}

DEBUG = os.environ.get("DEBUG", False).lower() == "true"
