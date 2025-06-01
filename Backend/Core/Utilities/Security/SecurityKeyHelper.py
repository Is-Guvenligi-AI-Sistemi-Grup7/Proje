from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.primitives.ciphers.aead import AESGCM
from cryptography.hazmat.backends import default_backend
import base64

class SecurityKeyHelper:
    @staticmethod
    def create_security_key(security_key: str) -> bytes:
        """
        C#'taki SymmetricSecurityKey karşılığı olarak,
        burada UTF-8 ile encode edilmiş anahtarı byte dizisi olarak döner.
        """
        return security_key.encode('utf-8')
