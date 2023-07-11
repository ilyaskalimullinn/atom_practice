from datetime import date
from typing import Optional

from sqlalchemy import Column, Integer, String, ForeignKey, Date, CheckConstraint, UniqueConstraint
from sqlalchemy.orm import declarative_base, relationship, validates

Base = declarative_base()


def string_column(name: str, max_length: int, min_length: int, **kwargs) -> Column:
    constraint_str = f"LENGTH({name}) >= {min_length}"
    column = Column(name, String(max_length), CheckConstraint(constraint_str), **kwargs)
    return column


class CarManufacturer(Base):
    __tablename__ = "car_manufacturer"

    id = Column(Integer, primary_key=True)
    name = string_column("name", max_length=255, min_length=1, nullable=False, unique=True)

    def __init__(self, id: int, name: str):
        self.id = id
        self.name = name

    def __repr__(self):
        return f"<CarManufacturer(id={self.id}, name={self.name})>"


class CarModel(Base):
    __tablename__ = "car_model"

    id = Column(Integer, primary_key=True)
    name = string_column("name", max_length=255, min_length=1, nullable=False)
    release_date = Column(Date, nullable=True)
    manufacturer_id = Column(ForeignKey("car_manufacturer.id", ondelete="CASCADE"), nullable=False)
    base_price = Column(Integer, CheckConstraint("base_price >= 0"), nullable=True)

    manufacturer = relationship("CarManufacturer")

    __table_args__ = (
        UniqueConstraint("name", "manufacturer_id", name="model_name_manufacturer_unique"),
    )

    def __init__(self, id: int, name: str, release_date: date, manufacturer_id: int, base_price: int):
        self.id = id
        self.name = name
        self.release_date = release_date
        self.manufacturer_id = manufacturer_id
        self.base_price = base_price

    def __repr__(self):
        return f"<CarModel(id={self.id}, name={self.name}, release_date={self.release_date} manufacturer_id={self.manufacturer_id})>"


class CarUsage(Base):
    __tablename__ = "car_usage"

    id = Column(Integer, primary_key=True)
    name = string_column("name", max_length=255, min_length=1, nullable=False, unique=True)

    def __init__(self, id: int, name: str):
        self.id = id
        self.name = name

    def __repr__(self):
        return f"<CarUsage(id={self.id}, name={self.name})>"


class Car(Base):
    __tablename__ = "car"

    id = Column(Integer, primary_key=True)
    plate_number = string_column("plate_number", max_length=32, min_length=1, nullable=False, unique=True)
    manufacture_date = Column(Date)
    mileage = Column(Integer, nullable=False, default=0)
    model_id = Column(ForeignKey("car_model.id", ondelete="CASCADE"), nullable=False)
    usage_id = Column(ForeignKey("car_usage.id", ondelete="SET NULL"), nullable=True)

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
