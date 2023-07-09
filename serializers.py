from typing import Optional

from db.models import CarManufacturer


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
