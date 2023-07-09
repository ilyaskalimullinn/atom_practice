from typing import List

from db.db import Session
from db.models import CarManufacturer


class CarManufacturerRepository:
    session: Session

    def __init__(self, session: Session) -> None:
        self.session = session

    def find_all(self) -> List[CarManufacturer]:
        return self.session.query(CarManufacturer).all()

    def create(self, manufacturer: CarManufacturer) -> None:
        self.session.add(manufacturer)
        self.session.commit()
