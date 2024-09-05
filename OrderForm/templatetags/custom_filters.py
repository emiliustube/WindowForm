from django import template

register = template.Library()

@register.filter
def floatmul(value, arg):
    """
    Multiplies two values after converting them to float.
    """
    try:
        return float(value) * float(arg)
    except (ValueError, TypeError):
        return ''  # Return empty string on error

@register.filter
def floatdiv(value, arg):
    """
    Divides value by arg after converting them to float.
    Handles division by zero and other conversion errors.
    """
    try:
        return float(value) / float(arg)
    except (ValueError, TypeError, ZeroDivisionError):
        return ''  # Return empty string on error

@register.filter
def multiply_three(value1, value2, value3):
    """
    Multiplies three values after converting them to float.
    """
    try:
        # Convert values to float and return the product of three values
        return float(value1) * float(value2) * float(value3)
    except (ValueError, TypeError):
        return 0  # Return 0 on error