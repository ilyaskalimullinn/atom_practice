from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import declarative_base

Base = declarative_base()


class CarManufacturer(Base):
    __tablename__ = "car_manufacturer"

    id = Column(Integer, primary_key=True)
    name = Column(String(255))

    def __init__(self, id, name):
        self.id = id
        self.name = name
