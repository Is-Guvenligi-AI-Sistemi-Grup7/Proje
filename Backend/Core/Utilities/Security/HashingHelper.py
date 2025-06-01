import hashlib
import hmac
import os

def create_password_hash(password: str):
    salt = os.urandom(32)
    hashed = hmac.new(salt, password.encode(), hashlib.sha512).digest()
    return hashed, salt

def verify_password_hash(password: str, password_hash: bytes, salt: bytes):
    new_hash = hmac.new(salt, password.encode(), hashlib.sha512).digest()
    return hmac.compare_digest(new_hash, password_hash)
