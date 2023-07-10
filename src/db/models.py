from datetime import date
from typing import Union

from sqlalchemy import Column, Integer, String, ForeignKey, Date
from sqlalchemy.orm import declarative_base, relationship, mapped_column

Base = declarative_base()


class CarManufacturer(Base):
    __tablename__ = "car_manufacturer"

    id = Column(Integer, primary_key=True)
    name = Column(String(255))

    def __init__(self, id, name):
        self.id = id
        self.name = name

    def __repr__(self):
        return f"<CarManufacturer(id={self.id}, name={self.name})>"


class CarModel(Base):
    __tablename__ = "car_model"

    id = Column(Integer, primary_key=True)
    name = Column(String(255))
    release_date = Column(Date)
    manufacturer_id = Column(ForeignKey("car_manufacturer.id", ondelete="CASCADE"))

    manufacturer = relationship("CarManufacturer")

    def __init__(self, id: int, name: str, release_date: date, manufacturer_id: int):
        self.id = id
        self.name = name
        self.release_date = release_date
        self.manufacturer_id = manufacturer_id

    def __repr__(self):
        return f"<CarModel(id={self.id}, name={self.name}, release_date={self.release_date} manufacturer_id={self.manufacturer_id})>"


class CarUsage(Base):
    __tablename__ = "car_usage"

    id = Column(Integer, primary_key=True)
    name = Column(String(255))

    def __init__(self, id, name):
        self.id = id
        self.name = name

    def __repr__(self):
        return f"<CarUsage(id={self.id}, name={self.name})>"
