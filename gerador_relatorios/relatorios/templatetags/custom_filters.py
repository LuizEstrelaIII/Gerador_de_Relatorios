from django import template

register = template.Library()

@register.filter
def multiply(value, arg):
    """Multiplica dois valores"""
    try:
        return value * arg
    except (TypeError, ValueError):
        return 0
