from typing import List
from datetime import datetime

# Assuming these are the equivalent classes in Python
class Neglect:
    def __init__(self):
        self.neglect_id = 0
        self.title = ""
        self.user_id = 0
        self.severity_level = 0.0

class NeglectDetailDto:
    pass

class Messages:
    NEGLECT_ADDED = "Neglect added"
    NEGLECTS_LISTED = "Neglects listed"
    MAINTENANCE_TIME = "Maintenance time"
    USER_ERROR = "User error"
    NEGLECT_TITLE_ALREADY_EXISTS = "Neglect title already exists"
    USER_LIMIT_EXCEEDED = "User limit exceeded"

class DataResult:
    def __init__(self, success: bool, data=None, message: str = ""):
        self.success = success
        self.data = data
        self.message = message

class Result:
    def __init__(self, success: bool, message: str = ""):
        self.success = success
        self.message = message

class SuccessDataResult(DataResult):
    def __init__(self, data=None, message: str = ""):
        super().__init__(True, data, message)

class ErrorDataResult(DataResult):
    def __init__(self, message: str = ""):
        super().__init__(False, None, message)

class SuccessResult(Result):
    def __init__(self, message: str = ""):
        super().__init__(True, message)

class ErrorResult(Result):
    def __init__(self, message: str = ""):
        super().__init__(False, message)

class BusinessRules:
    @staticmethod
    def run(*results):
        for result in results:
            if result and not result.success:
                return result
        return None

# Decorators to simulate aspects (simplified versions)
def cache_remove_aspect(pattern):
    def decorator(func):
        def wrapper(*args, **kwargs):
            # Cache removal logic here
            return func(*args, **kwargs)
        return wrapper
    return decorator

def secured_operation(roles):
    def decorator(func):
        def wrapper(*args, **kwargs):
            # Security check logic here
            return func(*args, **kwargs)
        return wrapper
    return decorator

def validation_aspect(validator_type):
    def decorator(func):
        def wrapper(*args, **kwargs):
            # Validation logic here
            return func(*args, **kwargs)
        return wrapper
    return decorator

def cache_aspect(func):
    def wrapper(*args, **kwargs):
        # Caching logic here
        return func(*args, **kwargs)
    return wrapper

def performance_aspect(duration):
    def decorator(func):
        def wrapper(*args, **kwargs):
            # Performance monitoring logic here
            return func(*args, **kwargs)
        return wrapper
    return decorator

def transaction_scope_aspect(func):
    def wrapper(*args, **kwargs):
        # Transaction logic here
        return func(*args, **kwargs)
    return wrapper

class NeglectManager:
    def __init__(self, neglect_dal, user_service):
        self._neglect_dal = neglect_dal
        self._user_service = user_service

    @cache_remove_aspect("INeglectService.Get")
    @secured_operation("neglect.add,admin")
    @validation_aspect("NeglectValidator")
    def add(self, neglect: Neglect) -> Result:
        result = BusinessRules.run(
            self._check_if_neglect_title_exists(neglect.title),
            self._check_if_neglect_count_of_user_correct(neglect.user_id),
            self._check_if_user_limit_exceeded()
        )

        if result is not None:
            return result

        self._neglect_dal.add(neglect)
        return SuccessResult(Messages.NEGLECT_ADDED)

    @cache_aspect
    def get_all(self) -> DataResult:
        # Business logic
        if datetime.now().hour == 21:
            return ErrorDataResult(Messages.MAINTENANCE_TIME)
        
        return SuccessDataResult(self._neglect_dal.get_all(), Messages.NEGLECTS_LISTED)

    def get_all_by_user_id(self, id: int) -> DataResult:
        neglects = self._neglect_dal.get_all(lambda n: n.user_id == id)
        return SuccessDataResult(neglects)

    def get_all_by_severity(self, min_severity: float, max_severity: float) -> DataResult:
        neglects = self._neglect_dal.get_all(lambda n: min_severity <= n.severity_level <= max_severity)
        return SuccessDataResult(neglects)

    @cache_aspect
    @performance_aspect(5)
    def get_by_id(self, neglect_id: int) -> DataResult:
        neglect = self._neglect_dal.get(lambda n: n.neglect_id == neglect_id)
        return SuccessDataResult(neglect)

    def get_neglect_details(self) -> DataResult:
        details = self._neglect_dal.get_neglects_details()
        return SuccessDataResult(details)

    @cache_remove_aspect("INeglectService.Get")
    @validation_aspect("NeglectValidator")
    def update(self, neglect: Neglect) -> Result:
        result = len(self._neglect_dal.get_all(lambda n: n.user_id == neglect.user_id))
        if result >= 10:
            return ErrorResult(Messages.USER_ERROR)
        
        self._neglect_dal.update(neglect)
        return SuccessResult(Messages.NEGLECT_ADDED)

    # Private methods - only for use within this class
    def _check_if_neglect_count_of_user_correct(self, user_id: int) -> Result:
        # Select count(*) from neglects where userId=1
        result = len(self._neglect_dal.get_all(lambda n: n.user_id == user_id))
        if result >= 10:
            return ErrorResult(Messages.USER_ERROR)
        return SuccessResult()

    def _check_if_neglect_title_exists(self, title: str) -> Result:
        result = any(self._neglect_dal.get_all(lambda n: n.title == title))
        if result:
            return ErrorResult(Messages.NEGLECT_TITLE_ALREADY_EXISTS)
        return SuccessResult()

    def _check_if_user_limit_exceeded(self) -> Result:
        result = self._user_service.get_all()
        if len(result.data) > 15:
            return ErrorResult(Messages.USER_LIMIT_EXCEEDED)
        return SuccessResult()

    @transaction_scope_aspect
    def add_transactional_test(self, neglect: Neglect) -> Result:
        raise NotImplementedError()