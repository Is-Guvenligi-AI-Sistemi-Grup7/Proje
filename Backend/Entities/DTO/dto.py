from dataclasses import dataclass
from datetime import datetime

@dataclass
class SafetyViolationDto:
    violation_id: int
    user_full_name: str
    camera_location: str
    violation_type: str
    timestamp: datetime


@dataclass
class UserDto:
    id: int
    full_name: str
    email: str


@dataclass
class CameraDto:
    id: int
    location: str
    ip_address: str
