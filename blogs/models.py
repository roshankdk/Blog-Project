from django.db import models
from django.db.models.base import ModelState
from django.db.models.query import MAX_GET_RESULTS

# Create your models here.
class Blog(models.Model):
    image = models.ImageField(upload_to="blogs/")
    title = models.CharField(max_length = 255)
    image2 = models.ImageField(upload_to='blogs/', blank=True, null=True)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
