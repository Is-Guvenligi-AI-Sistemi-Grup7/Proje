from sqlalchemy.orm import Session
from Entities.Concrete.ViolationType import Violation

class EfViolationDal:
    def __init__(self, db: Session):
        self.db = db

    def get_all_violations(self):
        return self.db.query(Violation).all()

    def add_violation(self, violation: Violation):
        self.db.add(violation)
        self.db.commit()
        self.db.refresh(violation)
        return violation
