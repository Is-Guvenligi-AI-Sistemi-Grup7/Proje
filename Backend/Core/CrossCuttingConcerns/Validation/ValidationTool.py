from abc import ABC, abstractmethod
from typing import Any, List

class ValidationError:
    def __init__(self, property_name: str, error_message: str):
        self.property_name = property_name
        self.error_message = error_message

class ValidationResult:
    def __init__(self, is_valid: bool, errors: List[ValidationError] = None):
        self.is_valid = is_valid
        self.errors = errors or []

class ValidationContext:
    def __init__(self, instance_to_validate: object):
        self.instance_to_validate = instance_to_validate

class IValidator(ABC):
    @abstractmethod
    def validate(self, context: ValidationContext) -> ValidationResult:
        pass

class ValidationException(Exception):
    def __init__(self, errors: List[ValidationError]):
        self.errors = errors
        super().__init__(str(errors))

class ValidationTool:
    @staticmethod
    def validate(validator: IValidator, entity: object) -> None:
        context = ValidationContext(entity)
        result = validator.validate(context)
        if not result.is_valid:
            raise ValidationException(result.errors)