from typing import Tuple

# Assuming these are the equivalent classes in Python
class User:
    def __init__(self):
        self.email = ""
        self.first_name = ""
        self.last_name = ""
        self.password_hash = b""
        self.password_salt = b""
        self.status = True

class UserForRegisterDto:
    def __init__(self):
        self.email = ""
        self.first_name = ""
        self.last_name = ""

class UserForLoginDto:
    def __init__(self):
        self.email = ""
        self.password = ""

class AccessToken:
    pass

class Messages:
    USER_REGISTERED = "User registered"
    USER_NOT_FOUND = "User not found"
    PASSWORD_ERROR = "Password error"
    SUCCESSFUL_LOGIN = "Successful login"
    USER_ALREADY_EXISTS = "User already exists"
    ACCESS_TOKEN_CREATED = "Access token created"

class HashingHelper:
    @staticmethod
    def create_password_hash(password: str) -> Tuple[bytes, bytes]:
        # Mock implementation - replace with actual hashing logic
        password_hash = password.encode('utf-8')
        password_salt = b'salt'
        return password_hash, password_salt
    
    @staticmethod
    def verify_password_hash(password: str, password_hash: bytes, password_salt: bytes) -> bool:
        # Mock implementation - replace with actual verification logic
        return password.encode('utf-8') == password_hash

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

class AuthManager:
    def __init__(self, user_service, token_helper):
        self._user_service = user_service
        self._token_helper = token_helper
    
    def register(self, user_for_register_dto: UserForRegisterDto, password: str) -> DataResult:
        password_hash, password_salt = HashingHelper.create_password_hash(password)
        
        user = User()
        user.email = user_for_register_dto.email
        user.first_name = user_for_register_dto.first_name
        user.last_name = user_for_register_dto.last_name
        user.password_hash = password_hash
        user.password_salt = password_salt
        user.status = True
        
        self._user_service.add(user)
        return SuccessDataResult(user, Messages.USER_REGISTERED)
    
    def login(self, user_for_login_dto: UserForLoginDto) -> DataResult:
        user_to_check = self._user_service.get_by_mail(user_for_login_dto.email)
        
        if user_to_check is None:
            return ErrorDataResult(Messages.USER_NOT_FOUND)
        
        if not HashingHelper.verify_password_hash(user_for_login_dto.password, 
                                                 user_to_check.password_hash, 
                                                 user_to_check.password_salt):
            return ErrorDataResult(Messages.PASSWORD_ERROR)
        
        return SuccessDataResult(user_to_check, Messages.SUCCESSFUL_LOGIN)
    
    def user_exists(self, email: str) -> Result:
        if self._user_service.get_by_mail(email) is not None:
            return ErrorResult(Messages.USER_ALREADY_EXISTS)
        return SuccessResult()
    
    def create_access_token(self, user: User) -> DataResult:
        claims = self._user_service.get_claims(user)
        access_token = self._token_helper.create_token(user, claims)
        return SuccessDataResult(access_token, Messages.ACCESS_TOKEN_CREATED)