from django.shortcuts import render
from django.utils import timezone
from django.views.generic import TemplateView, DetailView
from .models import Post

class IndexTemplateView(TemplateView):
  template_name = 'blog/index.html'

  def get_context_data(self, **kwargs):
     ctx = super(IndexTemplateView, self).get_context_data(**kwargs)
     ctx['posts'] = Post.objects.filter(published_at__lte=timezone.now())
     return ctx


class BlogDetail(DetailView):
  model = Post
  template_name = 'blog/blog_detail.html'
  queryset = Post.objects.all()