from typing import List, Optional

# Assuming these are the equivalent classes in Python
class User:
    def __init__(self):
        self.email = ""

class OperationClaim:
    pass

class UserManager:
    def __init__(self, user_dal):
        self._user_dal = user_dal

    def get_claims(self, user: User) -> List[OperationClaim]:
        return self._user_dal.get_claims(user)

    def add(self, user: User) -> None:
        self._user_dal.add(user)

    def get_by_mail(self, email: str) -> Optional[User]:
        return self._user_dal.get(lambda u: u.email == email)