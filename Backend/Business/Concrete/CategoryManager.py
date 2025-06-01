from typing import List

# Assuming these are the equivalent classes in Python
class Category:
    def __init__(self):
        self.category_id = 0

class Messages:
    CATEGORY_ADDED = "Category added"
    CATEGORY_LISTED = "Category listed"

class DataResult:
    def __init__(self, success: bool, data=None, message: str = ""):
        self.success = success
        self.data = data
        self.message = message

class SuccessDataResult(DataResult):
    def __init__(self, data=None, message: str = ""):
        super().__init__(True, data, message)

class CategoryManager:
    def __init__(self, category_dal):
        self._category_dal = category_dal
    
    def get_all(self) -> DataResult:
        return SuccessDataResult(self._category_dal.get_all(), Messages.CATEGORY_ADDED)
    
    def get_by_id(self, category_id: int) -> DataResult:
        category = self._category_dal.get(lambda c: c.category_id == category_id)
        return SuccessDataResult(category, Messages.CATEGORY_LISTED)