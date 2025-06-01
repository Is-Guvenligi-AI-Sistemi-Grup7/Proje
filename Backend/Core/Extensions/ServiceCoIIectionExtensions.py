from abc import ABC, abstractmethod
from typing import List

class IServiceCollection:
    pass

class ICoreModule(ABC):
    @abstractmethod
    def load(self, service_collection: IServiceCollection) -> None:
        pass

class ServiceTool:
    @staticmethod
    def create(service_collection: IServiceCollection) -> IServiceCollection:
        return service_collection

class ServiceCollectionExtensions:
    @staticmethod
    def add_dependency_resolvers(service_collection: IServiceCollection, modules: List[ICoreModule]) -> IServiceCollection:
        for module in modules:
            module.load(service_collection)
        return ServiceTool.create(service_collection)