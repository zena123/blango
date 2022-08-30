from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone
from django.views.generic import TemplateView, DetailView
from django.views.generic.edit import FormMixin
from django.urls import reverse
from .models import Post
from .forms import CommentForm

class IndexTemplateView(TemplateView):
  template_name = 'blog/index.html'

  def get_context_data(self, **kwargs):
     ctx = super(IndexTemplateView, self).get_context_data(**kwargs)
     ctx['posts'] = Post.objects.filter(published_at__lte=timezone.now())
     return ctx

def post_detail(request, slug):
  post = get_object_or_404(Post, slug=slug)
  if request.user.is_active:
    if request.method == "POST":
      comment_form = CommentForm(request.POST)
      if comment_form.is_valid():

        comment = comment_form.save(commit=False)
        comment.content_object = post
        comment.creator = request.user
        comment.save()
        return redirect(request.path_info)
    else:
        comment_form = CommentForm()
  else:
      comment_form = None
      return render(
        request, "blog/blog_detail.html", {"post": post, "comment_form": comment_form})


# use generic CBV better
#will follow guides for now
# class BlogDetail(FormMixin, DetailView):
#   model = Post
#   form_class = CommentForm
#   template_name = 'blog/blog_detail.html'
#   queryset = Post.objects.all()

  