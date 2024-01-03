from django.shortcuts import render
# listview will display objects as lists
# detailview will display objects with bits of detail
# "generic" implies that it is a common function 
from django.views.generic import ListView, DetailView,CreateView
from .models import Post
# Create your views here.
from .forms import PostForm


class HomeView(ListView):
    model = Post
    queryset = Post.objects.all()  # fetches all objects from Post
    template_name = 'index.html'
    context_object_name = 'posts'  # while rendering elements in html template 'posts' is used 

class ArticleDetail(DetailView):
    model = Post
    queryset = Post.objects.all()  # fetches all objects from Post
    template_name = 'article.html'
    context_object_name = 'post' # while rendering elements in html template 'posts' is used  
    
class AddPost(CreateView):
    model = Post
    template_name = 'addpost.html'
    form_class = PostForm
    #fields = '__all__' # take evrything from model title,body,etc    
    #fields = ('title', 'body')