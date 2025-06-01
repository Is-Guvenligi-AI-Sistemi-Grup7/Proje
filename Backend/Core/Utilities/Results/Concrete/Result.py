from Core.Utilities.Results.Abstract.IResult import IResult

class Result(IResult):
    def __init__(self, success: bool, message: str = None):
        self._success = success
        self._message = message

    @property
    def success(self) -> bool:
        return self._success

    @property
    def message(self) -> str:
        return self._message
