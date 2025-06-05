from abc import ABC, abstractmethod
from typing import List
from Entities.Concrete.ViolationType import SafetyViolation
from datetime import datetime

class ISafetyViolationDal(ABC):
    @abstractmethod
    def add(self, violation: SafetyViolation):
        pass

    @abstractmethod
    def get_all(self) -> List[SafetyViolation]:
        pass

    @abstractmethod
    def get_by_user_id(self, user_id: int) -> List[SafetyViolation]:
        pass

    @abstractmethod
    def get_by_date_range(self, start: datetime, end: datetime) -> List[SafetyViolation]:
        pass
