from abc import ABC

class IEntity(ABC):
    pass

class OperationClaim(IEntity):
    def __init__(self):
        self.id = None
        self.name = None