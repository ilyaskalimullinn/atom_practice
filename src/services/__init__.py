import abc
from typing import TypeVar, Generic, Type, List

from db.repositories import IModelCrudRepository
from exceptions import ServiceException
from serializers import IModelSerializer

T = TypeVar("T")


class BaseCrudService(Generic[T], abc.ABC):
    model_class: Type
    model_repository: IModelCrudRepository[T]

    def __init__(self,
                 model_repository: IModelCrudRepository[T],
                 model_class: Type) -> None:
        self.model_class = model_class
        self.model_repository = model_repository

    def find_all(self) -> List[T]:
        return self.model_repository.find_all()

    def create(self, serializer: IModelSerializer[T]) -> T:
        if not serializer.is_valid():
            raise ServiceException("Validation exception")
        if serializer.id is not None:
            raise ServiceException("Invalid id: must be empty")
        obj = serializer.to_obj()
        self.model_repository.save(obj)
        return obj

    def delete_by_id(self, id: int) -> T:
        obj = self.model_repository.find_by_id(id)
        if obj is None:
            raise ServiceException(f"No {self.model_class} with id {id}")
        return self.delete(obj)

    def delete(self, obj: T) -> T:
        self.model_repository.delete(obj)
        return obj

    def update(self, serializer: IModelSerializer[T]) -> T:
        if not serializer.is_valid():
            raise ServiceException("Validation exception")
        if serializer.id is None:
            raise ServiceException(f"Invalid {self.model_class} id")
        obj = serializer.to_obj()
        self.model_repository.save(obj)
        return self.model_repository.find_by_id(obj.id)
