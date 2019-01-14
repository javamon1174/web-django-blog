from django.shortcuts import render, get_object_or_404
from django.views.generic import TemplateView, DeleteView
from django.views.generic.list import ListView
from django.utils import timezone
from blog.models import *
from django.contrib.auth.models import User

from tagging.models import Tag, TaggedItem
from tagging.views import TaggedObjectList

class IndexView(TemplateView) :
    template_name = 'blog/index.html'

    def get_queryset(self):
        pass

class PostListView(ListView) :
    model = Post
    slug_field = "username"
    context_object_name = 'posts'
    paginate_by = 6

    def get_queryset(self, **kwargs):
        user = get_object_or_404(User, username=self.kwargs['username'])
        return Post.objects.filter(author=user)

class PostDetailView(DeleteView) :
    model = Post
    template_name = 'blog/post_detail.html'


# class PostTOL(TaggedObjectList) :
#     model = Post
#     template_name = 'tagging/tagging_post_list'
#
# class TagTV(TemplateView) :
#     template_name = 'tagging/tagging_tags.html'