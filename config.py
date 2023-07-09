import os

DATABASE = {
    "URL": os.environ.get("DB_URL", "postgresql+psycopg2://atom:atom@localhost:5432/atom"),
    "DEBUG": os.environ.get("DB_DEBUG", False)
}
