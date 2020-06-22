from django.shortcuts import render,redirect
from django.urls import reverse
from .models import Post
# Create your views here.
def home(request):
    post = Post.objects.all()
    return render(request, 'home.html', {'post':post})

def createPost(request):
    if request.method == "POST"  and request.FILES['image']:
        print(request.POST)
        image = request.FILES['image']
        title = request.POST["title"]
        content = request.POST["content"]
        if image!="":
            Post.objects.create(image=image, title=title, content=content)
        else:
            Post.objects.create(title=title, content=content)
        return redirect('home')
    else:
        return render(request, 'create.html')


def detail(request, id):
    post = Post.objects.get(id=id)
    if request.method == "POST":
        title = request.POST["title"]
        content = request.POST["content"]
        post.title=title 
        post.content=content
        post.save()
    return render(request, 'detail.html', {'post':post})

def deletePost(request, id):
    if request.method == "POST":
        post = Post.objects.get(id=id)
        post.delete()
    return redirect('home')