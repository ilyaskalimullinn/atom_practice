import abc
from typing import List, Optional, TypeVar, Generic, Type

from sqlalchemy.orm import joinedload

from db.db import Session
from db.models import CarManufacturer, CarModel


T = TypeVar("T")


class IModelCrudRepository(Generic[T], abc.ABC):
    @abc.abstractmethod
    def find_all(self) -> List[T]:
        pass

    @abc.abstractmethod
    def find_by_id(self, id: int) -> Optional[T]:
        pass

    @abc.abstractmethod
    def save(self, obj: T) -> None:
        pass

    @abc.abstractmethod
    def delete(self, obj: T) -> T:
        pass


class ICarManufacturerRepository(IModelCrudRepository[CarManufacturer], abc.ABC):
    pass


class ICarModelRepository(IModelCrudRepository[CarModel], abc.ABC):
    pass


class ModelCrudMixin(Generic[T]):
    session: Session
    klass: Type

    def __init__(self, session: Session, klass: Type) -> None:
        self.session = session
        self.klass = klass

    def find_all(self) -> List[T]:
        return self.session.query(self.klass).all()

    def save(self, obj: T) -> None:
        if obj.id is None:
            self.session.add(obj)
        else:
            self.session.merge(obj)
        self.session.commit()

    def find_by_id(self, id: int) -> Optional[T]:
        return self.session.get(self.klass, id)

    def delete(self, obj: T) -> None:
        self.session.delete(obj)
        self.session.commit()


class CarManufacturerRepository(ModelCrudMixin[CarManufacturer], ICarManufacturerRepository):
    def __init__(self, session: Session) -> None:
        super().__init__(session, CarManufacturer)


class CarModelRepository(ModelCrudMixin[CarModel], ICarModelRepository):
    def __init__(self, session: Session) -> None:
        super().__init__(session, CarModel)

    def find_all(self) -> List[CarModel]:
        return self.session.query(CarModel).options(joinedload(CarModel.manufacturer)).all()

    def find_by_id(self, id: int) -> Optional[CarModel]:
        return self.session.get(CarModel, id)
