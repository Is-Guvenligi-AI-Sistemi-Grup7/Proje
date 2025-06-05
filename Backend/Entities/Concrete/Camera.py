from dataclasses import dataclass

@dataclass
class Camera:
    camera_id: int
    name: str
    location: str
    ip_address: str
    rule_id: int
