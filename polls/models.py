from django.db import models
from django.contrib.auth.models import User

# The daily target


class User(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=254, unique=True)
    

    def __str__(self):
        return f'{self.name}'


class Habit(models.Model):
    habit = models.CharField(max_length=100)
    user = models.ForeignKey(
        'User', on_delete=models.SET_NULL, null=True,)
    description = models.TextField(max_length=500)
    daily_goal = models.TextField(max_length=200, default="goal",)
    slug = models.SlugField(null=False, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.habit}'

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        return super().save(*args, **kwargs)    
    


class Tracker(models.Model):
    person = models.ForeignKey('User', on_delete=models.SET_NULL, null=True,)
    habit_tracked = models.ForeignKey(
        'Habit', on_delete=models.SET_NULL, null=True,)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.person}'





# Create your models here.
