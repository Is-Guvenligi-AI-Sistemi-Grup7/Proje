from Core.Utilities.Interceptors import MethodInterceptionBaseAttribute
from Core.Utilities.Interceptors.Invocation import Invocation


class MethodInterception(MethodInterceptionBaseAttribute):
    def on_before(self, invocation: Invocation):
        pass

    def on_after(self, invocation: Invocation):
        pass

    def on_exception(self, invocation: Invocation, exception: Exception):
        pass

    def on_success(self, invocation: Invocation):
        pass

    def intercept(self, func):
        def wrapper(*args, **kwargs):
            invocation = Invocation(func, args, kwargs)
            is_success = True
            self.on_before(invocation)
            try:
                invocation.proceed()
            except Exception as e:
                is_success = False
                self.on_exception(invocation, e)
                raise
            finally:
                if is_success:
                    self.on_success(invocation)
                self.on_after(invocation)
            return invocation.result
        return wrapper
    
class Invocation:
    def __init__(self, func, args, kwargs):
        self.func = func
        self.args = args
        self.kwargs = kwargs
        self.result = None

    def proceed(self):
        self.result = self.func(*self.args, **self.kwargs)
