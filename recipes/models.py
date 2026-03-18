from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=65)
    def __str__(self):
        return self.name

    


class Recipe(models.Model):
    tittle = models.CharField(max_length=64)
    description = models.CharField(max_length=164)
    slug = models.SlugField()
    preparation_time = models.IntegerField()
    preparation_time_unit = models.CharField(max_length=65)
    sevings = models.IntegerField()
    sevings_unit = models.CharField(max_length=65)
    preparation_steps = models.TextField()
    preparation_steps_is_html = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_published = models.BooleanField(default=False)
    cover = models.ImageField(upload_to='recipes/cover/', blank=True, default=' ')
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null = True)
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null = True)

    def __str__(self):
        return self.tittle
    
    