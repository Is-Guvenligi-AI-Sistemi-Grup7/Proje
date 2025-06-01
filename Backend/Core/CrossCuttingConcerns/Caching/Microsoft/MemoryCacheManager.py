import re
import time
from typing import Any, Dict, Optional, TypeVar, Generic
from threading import Lock
from Core.Utilities.IoC import ServiceTool
from Core.CrossCuttingConcerns.Caching import ICacheManager

T = TypeVar('T')

class CacheEntry:
    def __init__(self, key: str, value: Any, expiry_time: float):
        self.key = key
        self.value = value
        self.expiry_time = expiry_time
    
    def is_expired(self) -> bool:
        return time.time() > self.expiry_time

class MemoryCache:
    def __init__(self):
        self._cache: Dict[str, CacheEntry] = {}
        self._lock = Lock()
    
    def set(self, key: str, value: Any, duration_minutes: int):
        expiry_time = time.time() + (duration_minutes * 60)
        with self._lock:
            self._cache[key] = CacheEntry(key, value, expiry_time)
    
    def get(self, key: str) -> Optional[Any]:
        with self._lock:
            if key in self._cache:
                entry = self._cache[key]
                if entry.is_expired():
                    del self._cache[key]
                    return None
                return entry.value
            return None
    
    def try_get_value(self, key: str) -> tuple[bool, Optional[Any]]:
        value = self.get(key)
        return value is not None, value
    
    def remove(self, key: str):
        with self._lock:
            if key in self._cache:
                del self._cache[key]
    
    def get_keys(self):
        with self._lock:
            # Clean expired entries first
            expired_keys = [key for key, entry in self._cache.items() if entry.is_expired()]
            for key in expired_keys:
                del self._cache[key]
            return list(self._cache.keys())

class MemoryCacheManager(ICacheManager):
    def __init__(self):
        self._memory_cache = ServiceTool.service_provider.get_service(MemoryCache)
        if self._memory_cache is None:
            self._memory_cache = MemoryCache()
    
    def add(self, key: str, value: Any, duration: int):
        self._memory_cache.set(key, value, duration)
    
    def get(self, key: str) -> Any:
        return self._memory_cache.get(key)
    
    def is_add(self, key: str) -> bool:
        success, _ = self._memory_cache.try_get_value(key)
        return success
    
    def remove(self, key: str):
        self._memory_cache.remove(key)
    
    def remove_by_pattern(self, pattern: str):
        # Get all current keys
        keys = self._memory_cache.get_keys()
        
        # Compile regex pattern
        regex = re.compile(pattern, re.IGNORECASE | re.SINGLELINE)
        
        # Find keys that match the pattern
        keys_to_remove = [key for key in keys if regex.search(str(key))]
        
        # Remove matching keys
        for key in keys_to_remove:
            self._memory_cache.remove(key)