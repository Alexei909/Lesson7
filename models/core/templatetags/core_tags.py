from django import template
from core.models import *

register = template.Library()

@register.simple_tag(name='phone')
def get_phone(filter=None):
    if not filter:
        return Phone.objects.all()
    else:
        return Phone.objects.filter(pk=filter)