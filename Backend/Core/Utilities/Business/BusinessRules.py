from abc import ABC, abstractmethod
from typing import List, Optional, Union


class IResult(ABC):
    """Abstract base class for result objects"""
    
    @property
    @abstractmethod
    def success(self) -> bool:
        """Returns whether the operation was successful"""
        pass
    
    @property
    @abstractmethod
    def message(self) -> str:
        """Returns the result message"""
        pass


class Result(IResult):
    """Concrete implementation of IResult"""
    
    def __init__(self, success: bool, message: str = ""):
        self._success = success
        self._message = message
    
    @property
    def success(self) -> bool:
        return self._success
    
    @property
    def message(self) -> str:
        return self._message


class BusinessRules:
    """Business rules utility class for validating multiple business logic conditions"""
    
    @staticmethod
    def run(*logics: IResult) -> Optional[IResult]:
        """
        Runs multiple business logic validations and returns the first failed result.
        
        Args:
            *logics: Variable number of IResult objects to validate
            
        Returns:
            The first failed IResult, or None if all validations pass
        """
        for logic in logics:
            if not logic.success:
                return logic
        return None
from abc import ABC, abstractmethod
from typing import List, Optional, Union


class IResult(ABC):
    """Abstract base class for result objects"""
    
    @property
    @abstractmethod
    def success(self) -> bool:
        """Returns whether the operation was successful"""
        pass
    
    @property
    @abstractmethod
    def message(self) -> str:
        """Returns the result message"""
        pass


class Result(IResult):
    """Concrete implementation of IResult"""
    
    def __init__(self, success: bool, message: str = ""):
        self._success = success
        self._message = message
    
    @property
    def success(self) -> bool:
        return self._success
    
    @property
    def message(self) -> str:
        return self._message


class BusinessRules:
    """Business rules utility class for validating multiple business logic conditions"""
    
    @staticmethod
    def run(*logics: IResult) -> Optional[IResult]:
        """
        Runs multiple business logic validations and returns the first failed result.
        
        Args:
            *logics: Variable number of IResult objects to validate
            
        Returns:
            The first failed IResult, or None if all validations pass
        """
        for logic in logics:
            if not logic.success:
                return logic
        return None
