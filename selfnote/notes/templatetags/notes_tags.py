from django import template
from django.template.defaultfilters import stringfilter
from django.utils.safestring import mark_safe
import re

register = template.Library()	

@register.filter(name='convert_to_nbsp')   
@stringfilter    
def convert_to_nbsp(string):
    string = re.sub('\s{2-4}', '&nbsp;'*4, string)
    string = re.sub('\t', '&nbsp;'*4, string)
    return mark_safe(string)