class MethodInterceptionBaseAttribute:
    def __init__(self, priority=0):
        self.priority = priority

    def intercept(self, invocation):
        pass
