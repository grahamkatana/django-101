from multiprocessing import context
from django.shortcuts import render
from post.models import Post
# Create your views here.

def index(request):
    data = Post.objects.all()
    context = {"data":data}
    return render(request,'pages/index.html',context=context)

def about(request):
    return render(request,'pages/about.html')
