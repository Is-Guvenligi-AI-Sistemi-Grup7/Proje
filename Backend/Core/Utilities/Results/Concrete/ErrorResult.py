from Core.Utilities.Results.Concrete.Result import Result

class ErrorResult(Result):
    def __init__(self, message: str = None):
        if message is not None:
            super().__init__(False, message)
        else:
            super().__init__(False)
