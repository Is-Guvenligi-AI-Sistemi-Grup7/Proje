from fastapi import FastAPI, HTTPException, Depends
from pydantic import BaseModel
from typing import List, Optional

app = FastAPI()

class Violation(BaseModel):
    id: Optional[int]
    camera_id: int
    violation_type: str
    date: str
    description: Optional[str] = None

class ViolationService:
    def __init__(self):
        self._violations = []
        self._next_id = 1

    def get_all(self):
        return {"Success": True, "Data": self._violations}

    def get_by_id(self, id: int):
        violation = next((v for v in self._violations if v.id == id), None)
        if violation:
            return {"Success": True, "Data": violation}
        return {"Success": False, "Message": "Violation not found"}

    def add(self, violation: Violation):
        violation.id = self._next_id
        self._next_id += 1
        self._violations.append(violation)
        return {"Success": True, "Message": "Violation added successfully"}

def get_violation_service():
    return ViolationService()

@app.get("/violations/getAll")
def get_all(violation_service: ViolationService = Depends(get_violation_service)):
    result = violation_service.get_all()
    if result["Success"]:
        return result
    raise HTTPException(status_code=400, detail="Failed to retrieve violations")

@app.get("/violations/getById")
def get_by_id(id: int, violation_service: ViolationService = Depends(get_violation_service)):
    result = violation_service.get_by_id(id)
    if result["Success"]:
        return result
    raise HTTPException(status_code=400, detail=result["Message"])

@app.post("/violations/add")
def add(violation: Violation, violation_service: ViolationService = Depends(get_violation_service)):
    result = violation_service.add(violation)
    if result["Success"]:
        return {"message": result["Message"]}
    raise HTTPException(status_code=400, detail=result["Message"])
