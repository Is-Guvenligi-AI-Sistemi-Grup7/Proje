from abc import ABC, abstractmethod
from typing import TypeVar, Generic, List, Callable, Optional

class IEntity(ABC):
    pass

T = TypeVar('T', bound=IEntity)

class IEntityRepository(ABC, Generic[T]):
    @abstractmethod
    def get_all(self, filter: Optional[Callable[[T], bool]] = None) -> List[T]:
        pass
    
    @abstractmethod
    def get(self, filter: Callable[[T], bool]) -> T:
        pass
    
    @abstractmethod
    def add(self, entity: T) -> None:
        pass
    
    @abstractmethod
    def update(self, entity: T) -> None:
        pass
    
    @abstractmethod
    def delete(self, entity: T) -> None:
        pass