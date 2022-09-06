import logging

from django import template
from django.contrib.auth import get_user_model
from django.utils.html import escape, format_html
from django.utils.safestring import mark_safe
from blog.models import Post

User =  get_user_model()

register = template.Library()
logger = logging.getLogger(__name__)


@register.filter
def author_details(author, current_user):
    if not isinstance(author, User):
        # return empty string as safe default
        return ""

    if author == current_user:
        return format_html("<strong>me</strong>")

    if author.first_name and author.last_name:
        name = f"{author.first_name} {author.last_name}"
    else:
        name = f"{author.username}"

    if author.email:
        prefix = format_html('<a href="mailto:{}">', author.email)
        suffix = format_html("</a>")
    else:
        prefix = ""
        suffix = ""

    return format_html('{}{}{}', prefix, name, suffix)



@register.simple_tag
def row(extra_classes=""):
    return format_html('<div class="row {}">', extra_classes)

@register.simple_tag    
def endrow():
    return format_html('</div>')


@register.simple_tag
def col(extra_classes=""):
    return format_html('<div class="col {}">', extra_classes)


@register.simple_tag
def endcol():
    return format_html("</div>")

@register.inclusion_tag("blog/post-list.html")
def recent_posts(post):
    print("hi")
    print(type(post))
    posts = Post.objects.exclude(pk=post.pk)[:5]
    logger.debug("Loaded %d recent posts", len(posts))
    return {"title": "Recent Posts", "posts": posts}