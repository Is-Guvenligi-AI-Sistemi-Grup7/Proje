from abc import ABC, abstractmethod

class IAuthService(ABC):
    
    @abstractmethod
    def register(self, user_for_register_dto, password: str):
        pass
    
    @abstractmethod
    def login(self, user_for_login_dto):
        pass
    
    @abstractmethod
    def user_exists(self, email: str):
        pass
    
    @abstractmethod
    def create_access_token(self, user):
        pass