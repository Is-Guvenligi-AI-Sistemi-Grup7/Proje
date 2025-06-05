from abc import ABC, abstractmethod
from typing import List
from Entities.Concrete.Notification import Notification

class INotificationDal(ABC):
    @abstractmethod
    def add(self, notification: Notification):
        pass

    @abstractmethod
    def get_by_manager_id(self, manager_id: int) -> List[Notification]:
        pass

    @abstractmethod
    def mark_as_read(self, notification_id: int):
        pass
