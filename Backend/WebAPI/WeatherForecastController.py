from fastapi import FastAPI
from pydantic import BaseModel
from typing import List
from datetime import datetime, timedelta
import random

app = FastAPI()

# Örnek ihlal seviyeleri
violation_levels = ["Low", "Medium", "High", "Critical"]

class ViolationReport(BaseModel):
    date: datetime
    violation_level: str
    description: str

@app.get("/violation-reports", response_model=List[ViolationReport])
def get_violation_reports():
    reports = []
    for i in range(5):
        report = ViolationReport(
            date=datetime.now() + timedelta(days=i+1),
            violation_level=random.choice(violation_levels),
            description=f"Ihlal açıklaması örneği {i+1}"
        )
        reports.append(report)
    return reports
