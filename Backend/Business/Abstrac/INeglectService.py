from abc import ABC, abstractmethod
from typing import List, Optional
from dataclasses import dataclass

# Assuming these are the equivalent classes/types in Python
class Neglect:
    pass

class NeglectDetailDto:
    pass

@dataclass
class Result:
    success: bool
    message: str = ""

@dataclass
class DataResult:
    success: bool
    data: any = None
    message: str = ""

class INeglectService(ABC):
    
    @abstractmethod
    def get_all(self) -> DataResult[List[Neglect]]:
        pass
    
    @abstractmethod
    def get_all_by_user_id(self, user_id: int) -> DataResult[List[Neglect]]:
        pass
    
    @abstractmethod
    def get_all_by_severity(self, min_severity: str, max_severity: str) -> DataResult[List[Neglect]]:
        pass
    
    @abstractmethod
    def get_neglect_details(self) -> DataResult[List[NeglectDetailDto]]:
        pass
    
    @abstractmethod
    def add(self, neglect: Neglect) -> Result:
        pass
    
    @abstractmethod
    def get_by_id(self, neglect_id: int) -> DataResult[Neglect]:
        pass
    
    @abstractmethod
    def update(self, neglect: Neglect) -> Result:
        pass
    
    @abstractmethod
    def add_transactional_test(self, neglect: Neglect) -> Result:
        pass