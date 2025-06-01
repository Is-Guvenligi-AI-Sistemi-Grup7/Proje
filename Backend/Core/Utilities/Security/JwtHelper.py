from datetime import datetime, timedelta
from typing import List
from Core.Entities.Concrete.OperationClaim import User, OperationClaim
from Core.Utilities.Security.AccessToken import AccessToken
from Core.Utilities.Security import SecurityKeyHelper, SigningCredentialsHelper
import jwt

class JwtHelper:
    def __init__(self, configuration):
        self.configuration = configuration
        self._token_options = configuration.get("TokenOptions", {})
        self._access_token_expiration = None

    def create_token(self, user: User, operation_claims: List[OperationClaim]) -> AccessToken:
        expiration_minutes = self._token_options.get("AccessTokenExpiration", 60)
        self._access_token_expiration = datetime.utcnow() + timedelta(minutes=expiration_minutes)
        security_key = SecurityKeyHelper.create_security_key(self._token_options.get("SecurityKey"))
        signing_credentials = SigningCredentialsHelper.create_signing_credentials(security_key)

        token = self._create_jwt_security_token(user, signing_credentials, operation_claims)

        return AccessToken(token=token, expiration=self._access_token_expiration)

    def _create_jwt_security_token(self, user: User, signing_credentials, operation_claims: List[OperationClaim]) -> str:
        payload = {
            "iss": self._token_options.get("Issuer"),
            "aud": self._token_options.get("Audience"),
            "exp": self._access_token_expiration,
            "nbf": datetime.utcnow(),
            "iat": datetime.utcnow(),
            "sub": str(user.id),
            "email": user.email,
            "name": f"{user.first_name} {user.last_name}",
            "roles": [claim.name for claim in operation_claims],
        }
        # PyJWT'de imzalama için secret key ve algoritma verilir.
        token = jwt.encode(payload, signing_credentials, algorithm="HS512")
        return token
