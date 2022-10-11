"""docstringBlog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
#from .views import index, blog_detail
from .views import PostListView, PostDetailView, create_post

urlpatterns = [
     path("articles/", PostListView.as_view(), name="blog-index"),
     path("articles/<int:pk>", PostDetailView.as_view(), name="blog-detail"),
     path("articles/new", create_post, name="blog-create-post")
]