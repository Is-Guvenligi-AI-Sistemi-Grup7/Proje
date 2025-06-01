from abc import ABC, abstractmethod

class IResult(ABC):
    @property
    @abstractmethod
    def success(self) -> bool:
        pass

    @property
    @abstractmethod
    def message(self) -> str:
        pass
