from django.contrib.admin import register
from django.urls import path
from blogs import views

urlpatterns = [
    path("",views.home,name='home'),
    path("post/",views.post,name='post'),
    path("postdetails/",views.postDetails,name='postDetails'),
]
 