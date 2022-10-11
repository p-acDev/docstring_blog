from django.shortcuts import render, redirect
from .models import Post
from django.views.generic import ListView, DetailView
from .forms import PostForm
from django.utils.text import slugify

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

def create_post(request):
    
    context = {}
    
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            
            # on pre crée l'objet pour qu'il ai un id etc ...
            post = Post.objects.create(title=form.cleaned_data["title"],
                                       content=form.cleaned_data["content"])

            # pour faire un slug automatique
            slug = slugify(form.cleaned_data["title"])
            post.slug = slug
            
            # la relation m2m est comme une list. Il faut ajouter à la liste chaque tag selectionné.
            for t in form.cleaned_data["tags"]:
                post.tag.add(t)
            
            post.save()
 
            return redirect("blog-index")
    
    else:    
    
        form = PostForm()
    
    context["form"] = form
    
    return render(request, "blog/create.html", context)

# CBV
class PostListView(ListView):
    model = Post
    template_name = "blog/index.html"
    context_object_name = "posts"
    
class PostDetailView(DetailView):
    model = Post
    template_name = "blog/detail.html"
    context_object_name = "post"
