from abc import ABC

class IEntity(ABC):
    pass

class User(IEntity):
    def __init__(self):
        self.id = None
        self.first_name = None
        self.last_name = None
        self.email = None
        self.password_salt = None
        self.password_hash = None
        self.status = None