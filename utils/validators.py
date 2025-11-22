import re

def validate_email(email):
    """Valida formato de email"""
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return re.match(pattern, email) is not None

def validate_phone(phone):
    """Valida formato de teléfono"""
    if not phone:
        return True
    pattern = r'^[\d\s\+\-\(\)]+$'
    return re.match(pattern, phone) is not None

def validate_number(value):
    """Valida que sea un número"""
    try:
        int(value)
        return True
    except ValueError:
        return False

def validate_required(value):
    """Valida que el campo no esté vacío"""
    return value is not None and str(value).strip() != ""
