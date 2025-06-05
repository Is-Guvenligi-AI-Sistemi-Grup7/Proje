from typing import List, Optional
from dataclasses import dataclass

@dataclass
class User:
    id: int
    first_name: str
    last_name: str
    email: str

class InMemoryUserDal:
    def __init__(self):
        self.users: List[User] = [
            User(id=1, first_name="Ali", last_name="Yılmaz", email="ali@example.com"),
            User(id=2, first_name="Ayşe", last_name="Demir", email="ayse@example.com"),
            User(id=3, first_name="Mehmet", last_name="Kara", email="mehmet@example.com"),
        ]

    def add(self, user: User):
        self.users.append(user)

    def delete(self, user_id: int):
        self.users = [u for u in self.users if u.id != user_id]

    def get_all(self) -> List[User]:
        return self.users

    def get_by_id(self, user_id: int) -> Optional[User]:
        for user in self.users:
            if user.id == user_id:
                return user
        return None

    def update(self, updated_user: User):
        for i, user in enumerate(self.users):
            if user.id == updated_user.id:
                self.users[i] = updated_user
                break
