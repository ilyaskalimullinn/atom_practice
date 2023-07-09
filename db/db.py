from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from config import DATABASE
from db.models import Base

engine = create_engine(DATABASE.get("URL"), echo=DATABASE.get("DEBUG"))
Session = sessionmaker(bind=engine)


def create_all_tables():
    Base.metadata.create_all(engine)
