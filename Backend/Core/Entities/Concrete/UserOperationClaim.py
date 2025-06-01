from abc import ABC

class IEntity(ABC):
    pass

class UserOperationClaim(IEntity):
    def __init__(self):
        self.id = None
        self.user_id = None
        self.operation_claim_id = None