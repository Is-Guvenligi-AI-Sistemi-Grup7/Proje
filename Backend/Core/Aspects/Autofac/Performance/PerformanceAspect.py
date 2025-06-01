import time
from Core.Utilities.Interceptors import MethodInterception
from Core.Utilities.IoC import ServiceTool

class PerformanceAspect(MethodInterception):
    def __init__(self, interval: int):
        self._interval = interval
        self._start_time = None
    
    def on_before(self, invocation):
        self._start_time = time.time()
    
    def on_after(self, invocation):
        end_time = time.time()
        elapsed_seconds = end_time - self._start_time
        
        if elapsed_seconds > self._interval:
            print(f"Performance : {invocation.method.declaring_type.full_name}.{invocation.method.name}-->{elapsed_seconds}")
        
        self._start_time = None