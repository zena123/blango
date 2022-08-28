from django import template
from django.contrib.auth import get_user_model
from django.utils.html import escape, format_html
from django.utils.safestring import mark_safe

User =  get_user_model()

register = template.Library()

@register.filter
def author_details(author, user=None):
    if not isinstance(author, User):
        # return empty string as safe default
        return ""
    if user and user == author:
        return format_html('<strong>me</strong>')
    if author.first_name and author.last_name:
        name = escape(f"{author.first_name} {author.last_name}")
    else:
        name = escape(f"{author.username}")

    if author.email:
        # email = escape(author.email)
        # prefix = f'<a href="mailto:{email}">'
        prefix = format_html('<a href="mailto:{}">', author.email)

        suffix = format_html("</a>")
    else:
        prefix = ""
        suffix = ""

    return format_html('{}{}{}', prefix, name, suffix)
