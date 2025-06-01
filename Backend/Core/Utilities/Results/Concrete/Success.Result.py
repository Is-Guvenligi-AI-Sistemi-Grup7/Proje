from Core.Utilities.Results.Concrete.Result import Result

class SuccessResult(Result):
    def __init__(self, message: str = None):
        if message is not None:
            super().__init__(True, message)
        else:
            super().__init__(True)
