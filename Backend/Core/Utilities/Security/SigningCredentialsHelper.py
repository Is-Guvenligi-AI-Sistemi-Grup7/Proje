from cryptography.hazmat.primitives import hashes, hmac
from cryptography.hazmat.backends import default_backend

class SigningCredentialsHelper:
    @staticmethod
    def create_signing_credentials(security_key: bytes) -> hmac.HMAC:
        """
        C#'daki SigningCredentials karşılığı olarak,
        burada HMAC SHA-512 imzalama için hmac nesnesi döndürülür.
        
        security_key: UTF-8 encoded bytes olarak gelen gizli anahtar.
        """
        return hmac.HMAC(security_key, hashes.SHA512(), backend=default_backend())
