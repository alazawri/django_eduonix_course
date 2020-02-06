from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import BlogArticle
from django.contrib.auth import authenticate, login

def index(request):
    blogs = BlogArticle.objects.all()
    if request.method == "POST":
        usname = request.POST['username']
        pwd = request.POST['password']
        user = authenticate(username=usname, password=pwd)
        if user is not None:
            login(request, user)
            return render(request, 'blog_app/index.html', {'blogs': blogs, 'user': user})
    return render(request, 'blog_app/index.html', {'blogs': blogs})


def create_blog(request):
    new_blog = BlogArticle()
    new_blog.title = request.POST['title']    
    new_blog.author = request.user
    new_blog.blog_content = request.POST['blog_content']
    new_blog.save()

    blogs = BlogArticle.objects.all

    return render(request, 'blog_app/index.html', {'blogs': blogs})
