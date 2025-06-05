from sqlalchemy.orm import Session
from IUserDal import IUserDal
import User, OperationClaim, UserOperationClaim


class SqlAlchemyUserDal(IUserDal):
    def __init__(self, session: Session):
        self.session = session

    def get_claims(self, user: User):
        result = (
            self.session.query(OperationClaim)
            .join(UserOperationClaim, OperationClaim.id == UserOperationClaim.operation_claim_id)
            .filter(UserOperationClaim.user_id == user.id)
            .all()
        )
        return result
