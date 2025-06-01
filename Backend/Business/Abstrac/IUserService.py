from abc import ABC, abstractmethod
from typing import List, Optional

# Assuming these are the equivalent classes in Python
class User:
    pass

class OperationClaim:
    pass

class IUserService(ABC):
    
    @abstractmethod
    def get_claims(self, user: User) -> List[OperationClaim]:
        pass
    
    @abstractmethod
    def add(self, user: User) -> None:
        pass
    
    @abstractmethod
    def get_by_mail(self, email: str) -> Optional[User]:
        pass