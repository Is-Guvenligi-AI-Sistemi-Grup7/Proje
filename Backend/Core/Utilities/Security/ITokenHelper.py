from abc import ABC, abstractmethod
from typing import List
from Core.Entities.Concrete.OperationClaim import User, OperationClaim
from Core.Utilities.Security.AccessToken import AccessToken

class ITokenHelper(ABC):
    @abstractmethod
    def create_token(self, user: User, operation_claims: List[OperationClaim]) -> AccessToken:
        pass
