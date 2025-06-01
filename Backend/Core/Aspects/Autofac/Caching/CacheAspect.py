import functools
from typing import Any, Callable
from Core.CrossCuttingConcerns.Caching import ICacheManager
from Core.Utilities.Interceptors.MethodInterception import MethodInterception
from Core.Utilities.IoC import ServiceTool

class CacheAspect(MethodInterception):
    def __init__(self, duration: int = 60):
        self._duration = duration
        self._cache_manager: ICacheManager = ServiceTool.service_provider.get_service(ICacheManager)
    
    def intercept(self, invocation):
        method_name = f"{invocation.method.reflected_type.full_name}.{invocation.method.name}"
        arguments = list(invocation.arguments)
        key = f"{method_name}({','.join(str(x) if x is not None else '<Null>' for x in arguments)})"
        
        if self._cache_manager.is_add(key):
            invocation.return_value = self._cache_manager.get(key)
            return
        
        invocation.proceed()
        self._cache_manager.add(key, invocation.return_value, self._duration)