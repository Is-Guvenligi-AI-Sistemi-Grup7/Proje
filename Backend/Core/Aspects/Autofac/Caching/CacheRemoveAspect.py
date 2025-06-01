from Core.CrossCuttingConcerns.Caching import ICacheManager
from Core.Utilities.Interceptors import MethodInterception
from Core.Utilities.IoC import ServiceTool

class CacheRemoveAspect(MethodInterception):
    def __init__(self, pattern: str):
        self._pattern = pattern
        self._cache_manager: ICacheManager = ServiceTool.service_provider.get_service(ICacheManager)
    
    def on_success(self, invocation):
        self._cache_manager.remove_by_pattern(self._pattern)