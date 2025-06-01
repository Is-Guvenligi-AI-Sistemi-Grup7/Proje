from abc import ABC, abstractmethod
from typing import Any, TypeVar

T = TypeVar('T')

class ICacheManager(ABC):
    
    @abstractmethod
    def get(self, key: str) -> T:
        pass
    
    @abstractmethod
    def get(self, key: str) -> object:
        pass
    
    @abstractmethod
    def add(self, key: str, value: object, duration: int) -> None:
        pass
    
    @abstractmethod
    def is_add(self, key: str) -> bool:
        pass
    
    @abstractmethod
    def remove(self, key: str) -> None:
        pass
    
    @abstractmethod
    def remove_by_pattern(self, pattern: str) -> None:
        pass