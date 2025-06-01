from typing import List, Any, Callable, Optional

# Product entity class
class Product:
    def __init__(self):
        self.product_name = ""
        self.unit_price = 0.0
        self.category_id = 0

class ValidationRule:
    def __init__(self, property_name: str, validator_func: Callable, message: str = ""):
        self.property_name = property_name
        self.validator_func = validator_func
        self.message = message
        self.condition: Optional[Callable] = None
    
    def when(self, condition: Callable):
        """Apply rule only when condition is met"""
        self.condition = condition
        return self
    
    def with_message(self, message: str):
        """Set custom validation message"""
        self.message = message
        return self

class AbstractValidator:
    def __init__(self):
        self.rules: List[ValidationRule] = []
    
    def rule_for(self, property_selector: Callable):
        """Create a rule for a property"""
        return RuleBuilder(self, property_selector)
    
    def add_rule(self, rule: ValidationRule):
        """Add a validation rule"""
        self.rules.append(rule)
    
    def validate(self, instance: Any) -> List[str]:
        """Validate an instance and return list of error messages"""
        errors = []
        
        for rule in self.rules:
            # Check if condition applies (if any)
            if rule.condition and not rule.condition(instance):
                continue
            
            # Get property value
            property_value = getattr(instance, rule.property_name)
            
            # Validate
            if not rule.validator_func(property_value, instance):
                error_msg = rule.message or f"Validation failed for {rule.property_name}"
                errors.append(error_msg)
        
        return errors

class RuleBuilder:
    def __init__(self, validator: AbstractValidator, property_selector: Callable):
        self.validator = validator
        self.property_name = self._get_property_name(property_selector)
    
    def _get_property_name(self, property_selector: Callable) -> str:
        # Simple implementation - in real world, this would be more sophisticated
        # For now, we'll assume the property name is passed as string
        return "property"  # This would need proper implementation
    
    def minimum_length(self, min_length: int):
        """Minimum length validation"""
        rule = ValidationRule(
            self.property_name,
            lambda value, _: len(str(value)) >= min_length,
            f"{self.property_name} must be at least {min_length} characters long"
        )
        self.validator.add_rule(rule)
        return self
    
    def not_empty(self):
        """Not empty validation"""
        rule = ValidationRule(
            self.property_name,
            lambda value, _: value is not None and str(value).strip() != "",
            f"{self.property_name} cannot be empty"
        )
        self.validator.add_rule(rule)
        return self
    
    def greater_than(self, min_value: float):
        """Greater than validation"""
        rule = ValidationRule(
            self.property_name,
            lambda value, _: float(value) > min_value,
            f"{self.property_name} must be greater than {min_value}"
        )
        self.validator.add_rule(rule)
        return self
    
    def greater_than_or_equal_to(self, min_value: float):
        """Greater than or equal to validation"""
        rule = ValidationRule(
            self.property_name,
            lambda value, _: float(value) >= min_value,
            f"{self.property_name} must be greater than or equal to {min_value}"
        )
        self.validator.add_rule(rule)
        return self
    
    def when(self, condition: Callable):
        """Apply validation only when condition is met"""
        if self.validator.rules:
            self.validator.rules[-1].when(condition)
        return self
    
    def with_message(self, message: str):
        """Set custom validation message"""
        if self.validator.rules:
            self.validator.rules[-1].with_message(message)
        return self

class NeglectValidator(AbstractValidator):
    def __init__(self):
        super().__init__()
        self._setup_rules()
    
    def _setup_rules(self):
        """Setup validation rules for Product"""
        # Product name minimum length
        self.add_rule(ValidationRule(
            "product_name",
            lambda value, _: len(str(value)) >= 2,
            "Product name must be at least 2 characters long"
        ))
        
        # Product name not empty
        self.add_rule(ValidationRule(
            "product_name",
            lambda value, _: value is not None and str(value).strip() != "",
            "Product name cannot be empty"
        ))
        
        # Unit price not empty
        self.add_rule(ValidationRule(
            "unit_price",
            lambda value, _: value is not None and value != "",
            "Unit price cannot be empty"
        ))
        
        # Unit price greater than 0
        self.add_rule(ValidationRule(
            "unit_price",
            lambda value, _: float(value) > 0,
            "Unit price must be greater than 0"
        ))
        
        # Unit price >= 10 when category is 1
        conditional_rule = ValidationRule(
            "unit_price",
            lambda value, _: float(value) >= 10,
            "Unit price must be at least 10 for category 1"
        )
        conditional_rule.condition = lambda product: product.category_id == 1
        self.add_rule(conditional_rule)
        
        # Commented out rule for starting with 'A'
        # self.add_rule(ValidationRule(
        #     "product_name",
        #     lambda value, _: self._start_with_a(str(value)),
        #     "Urunler A harfi ile baslamali"
        # ))
    
    def _start_with_a(self, value: str) -> bool:
        """Check if value starts with 'A'"""
        return value.upper().startswith("A")

# Usage example:
# validator = ProductValidator()
# product = Product()
# product.product_name = "Test Product"
# product.unit_price = 5.0
# product.category_id = 1
# errors = validator.validate(product)
# if errors:
#     print("Validation errors:", errors)