from dataclasses import dataclass
from datetime import datetime

@dataclass
class ViolationDetailDto:
    violation_id: int
    user_full_name: str
    violation_type_name: str
    camera_location: str
    notification_date: datetime
    is_read: bool
