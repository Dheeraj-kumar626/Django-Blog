from django.shortcuts import render
from django.http import HttpResponse
from .models import Posts
# Create your views here.
def index(request):
#    return HttpResponse('Hello From Posts')

    posts = Posts.objects.all()

    context={
        'title':'LatestPosts1',
        'posts':posts
    }

    return render(request,'posts/index.html',context)

def details(request,post_id):

    post=Posts.objects.get(id=post_id)

    context={
        'post' : post
    }

    return render(request,'posts/details.html',context)