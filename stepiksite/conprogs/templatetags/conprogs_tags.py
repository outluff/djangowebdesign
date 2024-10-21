from django import template
import conprogs.views as views

register = template.Library()


@register.simple_tag()
def get_prices():
    return views.prices_db
