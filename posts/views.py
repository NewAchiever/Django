from django.shortcuts import render
from .models import Posts


# Create your views here.
def getposts(request):
    posts = Posts.objects.all()
    context = {
        'posts': posts
    }
    return render(request, 'posts/posts.html' ,context)

