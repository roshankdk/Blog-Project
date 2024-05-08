from django.shortcuts import HttpResponse, render

# Create your views here.
def login(request):
    return HttpResponse("<h1>This is the login page</h1>".encode('utf-8'))

def register(request):
    return HttpResponse("<h1>This is the register page</h1>".encode('utf-8'))