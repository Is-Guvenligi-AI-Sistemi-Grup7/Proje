from typing import Type, List
from Core.Utilities.Interceptors.MethodInterceptionBaseAttribute import MethodInterceptionBaseAttribute


class AspectInterceptorSelector:
    def select_interceptors(self, cls: Type, method, interceptors: List):
        class_attributes = [
            attr for attr in getattr(cls, '__dict__', {}).values()
            if isinstance(attr, MethodInterceptionBaseAttribute)
        ]

        method_attributes = []
        if hasattr(cls, method.__name__):
            method_func = getattr(cls, method.__name__)
            if hasattr(method_func, '__dict__'):
                method_attributes = [
                    attr for attr in method_func.__dict__.values()
                    if isinstance(attr, MethodInterceptionBaseAttribute)
                ]

        class_attributes.extend(method_attributes)

        # Örnek: class_attributes.append(ExceptionLogAspect(FileLogger))  # tüm methodları loglar

        return sorted(class_attributes, key=lambda x: x.priority)
