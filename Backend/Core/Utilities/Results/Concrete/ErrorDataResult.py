from typing import TypeVar, Generic
from Core.Utilities.Results.Concrete.DataResult import DataResult

T = TypeVar('T')


class ErrorDataResult(DataResult[T], Generic[T]):
    def __init__(self, data: T = None, message: str = None):
        if data is not None and message is not None:
            super().__init__(data, False, message)
        elif data is not None:
            super().__init__(data, False)
        elif message is not None:
            super().__init__(None, False, message)
        else:
            super().__init__(None, False)
