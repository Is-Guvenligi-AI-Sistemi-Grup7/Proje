from typing import List

class JwtRegisteredClaimNames:
    EMAIL = "email"

class ClaimTypes:
    NAME = "name"
    NAME_IDENTIFIER = "nameidentifier"
    ROLE = "role"

class Claim:
    def __init__(self, type: str, value: str):
        self.type = type
        self.value = value

class ClaimExtensions:
    @staticmethod
    def add_email(claims: List[Claim], email: str) -> None:
        claims.append(Claim(JwtRegisteredClaimNames.EMAIL, email))
    
    @staticmethod
    def add_name(claims: List[Claim], name: str) -> None:
        claims.append(Claim(ClaimTypes.NAME, name))
    
    @staticmethod
    def add_name_identifier(claims: List[Claim], name_identifier: str) -> None:
        claims.append(Claim(ClaimTypes.NAME_IDENTIFIER, name_identifier))
    
    @staticmethod
    def add_roles(claims: List[Claim], roles: List[str]) -> None:
        for role in roles:
            claims.append(Claim(ClaimTypes.ROLE, role))