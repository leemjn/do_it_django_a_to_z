from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from .models import Post
from django.views.generic import ListView

class PostList(ListView):
    model = Post
    ordering = '-pk'


