from typing import List
from django.shortcuts import render
from .models import Post
from django.views.generic import ListView, DetailView

# Create your views here.
# FBV
# def index(request):
    
#     context = {}
    
#     posts = Post.objects.all()
#     context["posts"] = posts
    
#     return render(request, "blog/index.html", context)

# def blog_detail(request, pk):
    
#     context = {}
    
#     post = Post.objects.get(pk=pk)
#     context["post"] = post
    
#     return render(request, "blog/detail.html", context)

# CBV
class PostListView(ListView):
    model = Post
    template_name = "blog/index.html"
    context_object_name = "posts"
    
class PostDetailView(DetailView):
    model = Post
    template_name = "blog/detail.html"
    context_object_name = "post"
