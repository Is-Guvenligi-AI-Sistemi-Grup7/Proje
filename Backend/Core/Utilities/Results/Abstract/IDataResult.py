from abc import ABC, abstractmethod
from typing import Generic, TypeVar

from Core.Utilities.Business.BusinessRules import IResult

T = TypeVar('T')


class IDataResult(IResult, Generic[T], ABC):
    @property
    @abstractmethod
    def data(self) -> T:
        pass