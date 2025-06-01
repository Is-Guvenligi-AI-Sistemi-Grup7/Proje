from abc import ABC, abstractmethod

class ICoreModule(ABC):
    @abstractmethod
    def load(self, services_collection):
        pass
