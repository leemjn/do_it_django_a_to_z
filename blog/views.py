from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from .models import Post

def index(request):
    Posts = Post.objects.all()

    return render(
        request,
        'blog/index.html',
        {
            'posts':Posts,
        }
    )
def single_post_page(request,pk):
    post=Post.objects.get(pk=pk)

    return render(
        request,
        'blog/single_post_page.html',
        {
            'post': post,
        }
    )
