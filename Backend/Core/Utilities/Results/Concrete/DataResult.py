from typing import Generic, TypeVar

from Core.Utilities.Results.Abstract.IDataResult import IDataResult
from Core.Utilities.Results.Concrete.Result import Result

T = TypeVar('T')


class DataResult(Result, IDataResult[T], Generic[T]):
    def __init__(self, data: T, success: bool, message: str = None):
        super().__init__(success, message)
        self._data = data

    @property
    def data(self) -> T:
        return self._data
