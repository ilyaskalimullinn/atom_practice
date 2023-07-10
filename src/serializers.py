import abc
from datetime import date
from typing import Optional, TypeVar, Generic, Any

from db.models import CarManufacturer, CarModel, CarUsage, Car

T = TypeVar("T")


class IModelSerializer(Generic[T], abc.ABC):
    id: Any

    @abc.abstractmethod
    def is_valid(self) -> bool:
        pass

    @abc.abstractmethod
    def to_obj(self) -> T:
        pass


class CarManufacturerSerializer(IModelSerializer[CarManufacturer]):
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


class CarModelSerializer(IModelSerializer[CarModel]):
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


class CarUsageSerializer(IModelSerializer[CarUsage]):
    id: int
    name: str

    def __init__(self, id: Optional[int] = None, name: Optional[str] = None) -> None:
        self.id = id
        self.name = name

    def is_valid(self) -> bool:
        return self.name is not None \
            and len(self.name) > 0 \
            and (self.id is None or self.id > 0)

    def to_obj(self) -> CarUsage:
        return CarUsage(**self.__dict__)


class CarSerializer(IModelSerializer[Car]):
    id: int
    plate_number: str
    manufacture_date: date
    mileage: int
    model_id: int
    usage_id: int

    def __init__(self,
                 id: Optional[int] = None,
                 plate_number: Optional[str] = None,
                 manufacture_date: Optional[date] = None,
                 mileage: Optional[int] = None,
                 model_id: Optional[int] = None,
                 usage_id: Optional[int] = None) -> None:
        self.id = id
        self.plate_number= plate_number
        self.manufacture_date = manufacture_date
        self.mileage = mileage
        self.model_id = model_id
        self.usage_id = usage_id

    def is_valid(self) -> bool:
        return self.plate_number is not None \
                and (self.plate_number is None or len(self.plate_number) >= 3) \
                and self.mileage is not None \
                and self.mileage >= 0 \
                and self.model_id is not None

    def to_obj(self) -> Car:
        return Car(**self.__dict__)
