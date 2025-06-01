class TokenOptions:
    def __init__(self, audience: str = None, issuer: str = None, access_token_expiration: int = None, security_key: str = None):
        self.audience = audience
        self.issuer = issuer
        self.access_token_expiration = access_token_expiration
        self.security_key = security_key
