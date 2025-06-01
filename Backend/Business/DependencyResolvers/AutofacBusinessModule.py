from typing import Dict, Type, Any, TypeVar, Optional
import inspect

T = TypeVar('T')

class ServiceLifetime:
    SINGLETON = "singleton"
    TRANSIENT = "transient"

class DependencyContainer:
    def __init__(self):
        self._services: Dict[Type, tuple] = {}
        self._singletons: Dict[Type, Any] = {}
    
    def register(self, interface: Type[T], implementation: Type[T], lifetime: str = ServiceLifetime.TRANSIENT):
        """Register a service with its implementation"""
        self._services[interface] = (implementation, lifetime)
        return self
    
    def register_singleton(self, interface: Type[T], implementation: Type[T]):
        """Register a service as singleton"""
        return self.register(interface, implementation, ServiceLifetime.SINGLETON)
    
    def resolve(self, interface: Type[T]) -> T:
        """Resolve a service instance"""
        if interface not in self._services:
            raise ValueError(f"Service {interface.__name__} is not registered")
        
        implementation, lifetime = self._services[interface]
        
        if lifetime == ServiceLifetime.SINGLETON:
            if interface not in self._singletons:
                self._singletons[interface] = self._create_instance(implementation)
            return self._singletons[interface]
        else:
            return self._create_instance(implementation)
    
    def _create_instance(self, implementation: Type[T]) -> T:
        """Create an instance with dependency injection"""
        constructor = implementation.__init__
        sig = inspect.signature(constructor)
        
        args = []
        for param_name, param in sig.parameters.items():
            if param_name == 'self':
                continue
            
            if param.annotation != inspect.Parameter.empty:
                dependency = self.resolve(param.annotation)
                args.append(dependency)
        
        return implementation(*args)

# Global container instance
container = DependencyContainer()

def configure_services():
    """Configure all service dependencies"""
    # Register services with their implementations
    container.register_singleton('IProductService', 'ProductManager')
    container.register_singleton('IProductDal', 'EfProductDal')
    container.register_singleton('ICategoryService', 'CategoryManager')
    container.register_singleton('ICategoryDal', 'EfCategoryDal')
    container.register('IUserService', 'UserManager')
    container.register('IUserDal', 'EfUserDal')
    container.register('IAuthService', 'AuthManager')
    container.register('ITokenHelper', 'JwtHelper')
    
    # Note: Aspect interceptor functionality would need to be implemented
    # separately using decorators or metaclasses in Python

class AutofacBusinessModule:
    """Python equivalent of Autofac business module"""
    
    @staticmethod
    def load():
        """Load all dependency registrations"""
        configure_services()
        return container

# Usage example:
# container = AutofacBusinessModule.load()
# product_service = container.resolve('IProductService')