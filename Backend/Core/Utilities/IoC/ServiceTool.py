class ServiceTool:
    service_provider = None

    @staticmethod
    def create(services_collection):
        """
        services_collection: bir bağımlılık listesi ya da DI konteyner olabilir
        """
        # Basit örnek olarak doğrudan atama yapıyoruz
        ServiceTool.service_provider = services_collection
        return services_collection

    def log_interceptor(func):
        def wrapper(*args, **kwargs):
            print(f"[INFO] Calling {func.__name__}")
            result = func(*args, **kwargs)
            print(f"[INFO] {func.__name__} returned {result}")
            return result
        return wrapper

    @log_interceptor
    def hello():
        return "hello world"
