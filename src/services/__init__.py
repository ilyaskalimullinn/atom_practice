import abc
from typing import TypeVar, Generic, Type, List, Optional

from db.repositories import IModelCrudRepository
from exceptions import ServiceException, DbUniqueException
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

    def find_by_id(self, id) -> Optional[T]:
        return self.model_repository.find_by_id(id)

    def create(self, serializer: IModelSerializer[T]) -> T:
        if not serializer.is_valid():
            raise ServiceException("Validation exception")
        if serializer.id is not None:
            raise ServiceException("Invalid id: must be empty")
        try:
            obj = serializer.to_obj()
            self.model_repository.save(obj)
            return obj
        except DbUniqueException as e:
            raise ServiceException(str(e))

    def delete_by_id(self, id: int) -> T:
        obj = self.model_repository.find_for_deletion_by_id(id)
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
        try:
            obj = serializer.to_obj()
            self.model_repository.save(obj)
            return self.model_repository.find_by_id(obj.id)
        except DbUniqueException as e:
            raise ServiceException(str(e))
