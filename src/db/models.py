from datetime import date
from typing import Union, Optional

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


class Car(Base):
    __tablename__ = "car"

    id = Column(Integer, primary_key=True)
    plate_number = Column(String(32))
    manufacture_date = Column(Date)
    mileage = Column(Integer)
    model_id = Column(ForeignKey("car_model.id", ondelete="CASCADE"))
    usage_id = Column(ForeignKey("car_usage.id", ondelete="SET NULL"))

    model = relationship("CarModel")
    usage = relationship("CarUsage")

    def __init__(self,
                 id: int,
                 plate_number: str,
                 manufacture_date: date,
                 mileage: int,
                 model_id: Optional[int] = None,
                 usage_id: Optional[int] = None) -> None:
        self.id = id
        self.plate_number= plate_number
        self.manufacture_date = manufacture_date
        self.mileage = mileage
        self.model_id = model_id
        self.usage_id = usage_id

    def __repr__(self):
        return f"<Car(id={self.id}, plate={self.plate_number})>"
