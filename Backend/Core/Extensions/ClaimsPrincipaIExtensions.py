from typing import List, Optional

class Claim:
    def __init__(self, type: str, value: str):
        self.type = type
        self.value = value

class ClaimTypes:
    ROLE = "role"

class ClaimsPrincipal:
    def __init__(self, claims: List[Claim] = None):
        self._claims = claims or []
    
    def find_all(self, claim_type: str) -> List[Claim]:
        return [claim for claim in self._claims if claim.type == claim_type]

class ClaimsPrincipalExtensions:
    @staticmethod
    def claims(claims_principal: Optional[ClaimsPrincipal], claim_type: str) -> Optional[List[str]]:
        if claims_principal is None:
            return None
        result = [claim.value for claim in claims_principal.find_all(claim_type)]
        return result
    
    @staticmethod
    def claim_roles(claims_principal: Optional[ClaimsPrincipal]) -> Optional[List[str]]:
        return ClaimsPrincipalExtensions.claims(claims_principal, ClaimTypes.ROLE)