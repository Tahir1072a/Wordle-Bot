from abc import ABC, abstractmethod
from typing import Generic, TypeVar, Optional

T = TypeVar('T')
K = TypeVar('K')

class ABaseRepository(Generic[T], ABC):

    @abstractmethod
    def create(self, entity: T) -> Optional[T]:
        pass
    @abstractmethod
    def delete(self, entity_id: int) -> bool:
        pass
    @abstractmethod
    def update(self, entity: T) -> bool:
        pass
    @abstractmethod
    def get_all(self) -> list[T]:
        pass