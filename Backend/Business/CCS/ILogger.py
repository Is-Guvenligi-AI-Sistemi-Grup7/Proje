from abc import ABC, abstractmethod

class ILogger(ABC):
    
    @abstractmethod
    def log(self) -> None:
        pass