from typing import List
from sqlalchemy.orm import Session

from Entities.Concrete.ViolationType import SafetyViolation
from Entities.Concrete.Camera import Camera
from Entities.Concrete.User import User
from Entities.DTO.ViolationDetailDto import ViolationDetailDto


class SqlAlchemySafetyViolationDal:
    def __init__(self, session: Session):
        self.session = session

    def get_safety_violation_details(self) -> List[ViolationDetailDto]:
        result = (
            self.session.query(
                User.full_name,
                SafetyViolation.violation_type,
                Camera.name,
                SafetyViolation.timestamp
            )
            .join(SafetyViolation, SafetyViolation.user_id == User.id)
            .join(Camera, SafetyViolation.camera_id == Camera.id)
            .all()
        )

        return [
            ViolationDetailDto(
                user_full_name=row[0],
                violation_type=row[1],
                camera_name=row[2],
                timestamp=row[3]
            ) for row in result
        ]
