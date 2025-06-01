from abc import ABC, abstractmethod
from typing import Type, Any
from Core.Utilities.Interceptors import MethodInterception
from Core.CrossCuttingConcerns.Validation import ValidationTool

class IValidator(ABC):
    @abstractmethod
    def validate(self, entity: Any):
        pass

class ValidationAspect(MethodInterception):
    def __init__(self, validator_type: Type):
        if not issubclass(validator_type, IValidator):
            raise Exception("Bu bir doğrulama sınıfı değil!")
        self._validator_type = validator_type
    
    def on_before(self, invocation):
        validator = self._validator_type()  # Create instance of validator
        
        # Get entity type from validator's generic base type
        # This is a simplified approach - you might need to adjust based on your validator structure
        entity_type = self._get_entity_type_from_validator()
        
        # Filter arguments that match the entity type
        entities = [arg for arg in invocation.arguments if isinstance(arg, entity_type)]
        
        for entity in entities:
            ValidationTool.validate(validator, entity)
    
    def _get_entity_type_from_validator(self):
        # This is a simplified implementation
        # You might need to implement this based on your specific validator structure
        # For example, if your validators have a specific naming convention or base class
        
        # One approach could be to use type hints or annotations
        if hasattr(self._validator_type, '__orig_bases__'):
            for base in self._validator_type.__orig_bases__:
                if hasattr(base, '__args__'):
                    return base.__args__[0]
        
        # Fallback - you might need to implement this differently
        return object