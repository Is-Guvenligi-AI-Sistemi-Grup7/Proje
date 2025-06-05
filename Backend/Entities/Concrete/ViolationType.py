from sqlalchemy import Column, Integer, String, DateTime
from DataAccess.Concrete.database import Base

class Violation(Base):
    __tablename__ = "violations"

    id = Column(Integer, primary_key=True, index=True)
    violation_type = Column(String, index=True)
    description = Column(String)
    date = Column(DateTime)
