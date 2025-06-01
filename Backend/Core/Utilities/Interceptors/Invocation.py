class Invocation:
    def __init__(self, func, args, kwargs):
        self.func = func
        self.args = args
        self.kwargs = kwargs
        self.result = None

    def proceed(self):
        self.result = self.func(*self.args, **self.kwargs)

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
