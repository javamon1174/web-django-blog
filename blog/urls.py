"""website URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from .views import *

app_name = 'blog'

# url 규칙
# /user_id/ => post_list
# /user_id/post/ => 위와 동일
# /user_id/post/slug => post_detail

# /post/create
# /post/slug/update
# /post/slug/delete

# /contents/ => content_list
# /content/99/ => content_detail

# /content/99/update
# /content/99/delete

# /user_id/tags/ => tag_cloud
# /user_id/tag/1 => tag_detail


urlpatterns = [
    path('', IndexView.as_view(), name="index"), # post list
    # path('<int:author_id>/', PostListView.as_view(), name='post_list'),
    path('<str:username>/', PostListView.as_view(), name='post_list'),
    path('<str:username>/<int:pk>', PostDetailView.as_view(), name='post_detail'),
]
