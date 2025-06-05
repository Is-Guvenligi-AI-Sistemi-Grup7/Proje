from typing import List, Optional
from dataclasses import dataclass
from datetime import datetime

@dataclass
class SafetyViolation:
    id: int
    user_id: int
    camera_id: int
    violation_type: str  # örn: 'helmet', 'glasses'
    timestamp: datetime

class InMemorySafetyViolationDal:
    def __init__(self):
        self.violations: List[SafetyViolation] = [
            SafetyViolation(id=1, user_id=1, camera_id=101, violation_type="helmet", timestamp=datetime.now()),
            SafetyViolation(id=2, user_id=2, camera_id=102, violation_type="glasses", timestamp=datetime.now()),
            SafetyViolation(id=3, user_id=3, camera_id=103, violation_type="helmet", timestamp=datetime.now()),
        ]

    def add(self, violation: SafetyViolation):
        self.violations.append(violation)

    def delete(self, violation_id: int):
        self.violations = [v for v in self.violations if v.id != violation_id]

    def get_all(self) -> List[SafetyViolation]:
        return self.violations

    def get_by_user(self, user_id: int) -> List[SafetyViolation]:
        return [v for v in self.violations if v.user_id == user_id]

    def get_by_camera(self, camera_id: int) -> List[SafetyViolation]:
        return [v for v in self.violations if v.camera_id == camera_id]

    def update(self, updated_violation: SafetyViolation):
        for i, violation in enumerate(self.violations):
            if violation.id == updated_violation.id:
                self.violations[i] = updated_violation
                break
