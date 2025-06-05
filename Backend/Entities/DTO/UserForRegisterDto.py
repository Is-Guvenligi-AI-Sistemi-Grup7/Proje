from dataclasses import dataclass

@dataclass
class UserForRegisterDto:
    email: str
    password: str
    first_name: str
    last_name: str
