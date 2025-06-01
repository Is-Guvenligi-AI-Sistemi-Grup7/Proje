from abc import ABC, abstractmethod
from typing import List

class ICategoryService(ABC):
    
    @abstractmethod
    def get_all(self) -> 'IDataResult[List[Category]]':
        pass
    
    @abstractmethod
    def get_by_id(self, category_id: int) -> 'IDataResult[Category]':
        pass