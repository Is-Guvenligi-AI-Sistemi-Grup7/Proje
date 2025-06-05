from typing import List, Optional
from dataclasses import dataclass

@dataclass
class Camera:
    id: int
    location: str
    ip_address: str

class InMemoryCameraDal:
    def __init__(self):
        self.cameras: List[Camera] = [
            Camera(id=101, location="Entrance Gate", ip_address="192.168.1.10"),
            Camera(id=102, location="Warehouse", ip_address="192.168.1.11"),
            Camera(id=103, location="Production Hall", ip_address="192.168.1.12"),
        ]

    def add(self, camera: Camera):
        self.cameras.append(camera)

    def delete(self, camera_id: int):
        self.cameras = [c for c in self.cameras if c.id != camera_id]

    def get_all(self) -> List[Camera]:
        return self.cameras

    def get_by_id(self, camera_id: int) -> Optional[Camera]:
        for camera in self.cameras:
            if camera.id == camera_id:
                return camera
        return None

    def update(self, updated_camera: Camera):
        for i, camera in enumerate(self.cameras):
            if camera.id == updated_camera.id:
                self.cameras[i] = updated_camera
                break
