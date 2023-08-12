from django import template

register = template.Library()


@register.simple_tag
def mediapath(file_path):
    media_prefix = "/media/"
    full_url = f"{media_prefix}{file_path}"
    return full_url
