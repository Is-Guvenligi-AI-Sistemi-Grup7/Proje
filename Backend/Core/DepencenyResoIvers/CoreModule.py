from abc import ABC, abstractmethod
from typing import Dict, Any

class IServiceCollection:
    def __init__(self):
        self.services = {}
    
    def add_singleton(self, interface_type: type, implementation_type: type) -> None:
        self.services[interface_type] = implementation_type
    
    def add_memory_cache(self) -> None:
        pass

class ICoreModule(ABC):
    @abstractmethod
    def load(self, services_collection: IServiceCollection) -> None:
        pass

class IHttpContextAccessor(ABC):
    pass

class HttpContextAccessor(IHttpContextAccessor):
    pass

class ICacheManager(ABC):
    pass

class MemoryCacheManager(ICacheManager):
    pass

class CoreModule(ICoreModule):
    def load(self, services_collection: IServiceCollection) -> None:
        services_collection.add_memory_cache()
        services_collection.add_singleton(IHttpContextAccessor, HttpContextAccessor)
        services_collection.add_singleton(ICacheManager, MemoryCacheManager)