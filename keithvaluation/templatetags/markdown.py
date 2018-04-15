from __future__ import absolute_import
from django import template
from django.template.defaultfilters import stringfilter
import markdown as mdlib

register = template.Library()

@register.filter(name='markdown', is_safe=True)
def markdown(value):
    return mdlib.markdown(value)
