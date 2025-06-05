from fastapi import FastAPI, HTTPException, Depends
from pydantic import BaseModel
from typing import List, Optional

app = FastAPI()

class Camera(BaseModel):
    id: Optional[int]
    location: str
    ip_address: str
    status: Optional[str] = "active"  # aktif/pasif gibi

class CameraService:
    def __init__(self):
        self._cameras = []
        self._next_id = 1

    def get_all(self):
        return {"Success": True, "Data": self._cameras}

    def get_by_id(self, id: int):
        camera = next((c for c in self._cameras if c.id == id), None)
        if camera:
            return {"Success": True, "Data": camera}
        return {"Success": False, "Message": "Camera not found"}

    def add(self, camera: Camera):
        camera.id = self._next_id
        self._next_id += 1
        self._cameras.append(camera)
        return {"Success": True, "Message": "Camera added successfully"}

def get_camera_service():
    return CameraService()

@app.get("/cameras/getAll")
def get_all_cameras(camera_service: CameraService = Depends(get_camera_service)):
    result = camera_service.get_all()
    if result["Success"]:
        return result
    raise HTTPException(status_code=400, detail="Failed to retrieve cameras")

@app.get("/cameras/getById")
def get_camera_by_id(id: int, camera_service: CameraService = Depends(get_camera_service)):
    result = camera_service.get_by_id(id)
    if result["Success"]:
        return result
    raise HTTPException(status_code=400, detail=result["Message"])

@app.post("/cameras/add")
def add_camera(camera: Camera, camera_service: CameraService = Depends(get_camera_service)):
    result = camera_service.add(camera)
    if result["Success"]:
        return {"message": result["Message"]}
    raise HTTPException(status_code=400, detail=result["Message"])
