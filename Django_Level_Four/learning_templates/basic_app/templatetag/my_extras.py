from atexit import register
from django import template

register = template.Library()

@register.filter(name='cut')
def cut(value, arg):
    """
    This cuts out all values of "args" from the strong!
    """

    return value.replace(arg,'')

#register.filter('cut', cut)
