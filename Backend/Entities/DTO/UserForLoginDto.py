from dataclasses import dataclass

@dataclass
class UserForLoginDto:
    email: str
    password: str
