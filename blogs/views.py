from django.http import HttpResponse
from django.shortcuts import render
from .models import Blog

# Create your views here.

def home(request):
    blog = Blog.objects.all()
    return render(request,'index.html',{'blog':blog})

def post(request):
    return HttpResponse("<h1>This is the post page</h1>".encode('utf-8'))

def postDetails(request):
    return HttpResponse("<h1>This is the postDetails page</h1>".encode('utf-8'))