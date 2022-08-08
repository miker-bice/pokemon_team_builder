from django import template

register = template.Library()

@register.filter(name='zip')
def zip_lists(var1, var2):
    return zip(var1, var2)