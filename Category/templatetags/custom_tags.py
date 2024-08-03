from django import template
from Category.models import Category

register = template.Library()

@register.simple_tag
def get_categories():
    cat=Category.objects.filter(parent__isnull=True).prefetch_related('subcategories')

    return cat
