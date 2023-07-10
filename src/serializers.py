from datetime import date
from typing import Optional

from db.models import CarManufacturer, CarModel


class CarManufacturerSerializer:
    id: int
    name: str

    def __init__(self, id: Optional[int] = None, name: Optional[str] = None) -> None:
        self.id = id
        self.name = name

    def is_valid(self) -> bool:
        return self.name is not None \
            and len(self.name) > 0 \
            and (self.id is None or self.id > 0)

    def to_obj(self) -> CarManufacturer:
        return CarManufacturer(self.id, self.name)


class CarModelSerializer:
    id: int
    name: str
    release_date: date
    manufacturer_id: int

    def __init__(self,
                 id: Optional[int] = None,
                 name: Optional[str] = None,
                 release_date: Optional[date] = None,
                 manufacturer_id: Optional[int] = None) -> None:
        self.id = id
        self.name = name
        self.release_date = release_date
        self.manufacturer_id = manufacturer_id

    def is_valid(self) -> bool:
        return self.name is not None \
            and len(self.name) > 0 \
            and (self.id is None or self.id > 0) \
            and self.manufacturer_id is not None \
            and self.release_date is not None

    def to_obj(self) -> CarModel:
        return CarModel(self.id, self.name, self.release_date, self.manufacturer_id)
