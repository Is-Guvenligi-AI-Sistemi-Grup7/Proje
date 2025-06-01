from abc import ABC, abstractmethod
from typing import TypeVar, Generic, List, Callable, Optional

TEntity = TypeVar('TEntity')
TContext = TypeVar('TContext')

class IEntity(ABC):
    pass

class IEntityRepository(ABC, Generic[TEntity]):
    @abstractmethod
    def add(self, entity: TEntity) -> None:
        pass
    
    @abstractmethod
    def delete(self, entity: TEntity) -> None:
        pass
    
    @abstractmethod
    def get(self, filter_func: Callable[[TEntity], bool]) -> Optional[TEntity]:
        pass
    
    @abstractmethod
    def get_all(self, filter_func: Optional[Callable[[TEntity], bool]] = None) -> List[TEntity]:
        pass
    
    @abstractmethod
    def update(self, entity: TEntity) -> None:
        pass

class EfEntityRepositoryBase(IEntityRepository[TEntity], Generic[TEntity, TContext]):
    def __init__(self, context_class: type):
        self.context_class = context_class
    
    def add(self, entity: TEntity) -> None:
        with self.context_class() as context:
            context.add(entity)
            context.commit()
    
    def delete(self, entity: TEntity) -> None:
        with self.context_class() as context:
            context.delete(entity)
            context.commit()
    
    def get(self, filter_func: Callable[[TEntity], bool]) -> Optional[TEntity]:
        with self.context_class() as context:
            return context.query(TEntity).filter(filter_func).first()
    
    def get_all(self, filter_func: Optional[Callable[[TEntity], bool]] = None) -> List[TEntity]:
        with self.context_class() as context:
            if filter_func is None:
                return context.query(TEntity).all()
            else:
                return context.query(TEntity).filter(filter_func).all()
    
    def update(self, entity: TEntity) -> None:
        with self.context_class() as context:
            context.merge(entity)
            context.commit()