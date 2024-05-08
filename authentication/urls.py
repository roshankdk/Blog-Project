from django.contrib.admin import register
from django.urls import path
from authentication import views
urlpatterns = [
    path("login/",views.login,name='login'),
    path("register/",views.register,name='register'),
]
