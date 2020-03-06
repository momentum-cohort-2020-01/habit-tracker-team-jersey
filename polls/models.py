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
    habit_user = models.ForeignKey(
        'User', on_delete=models.SET_NULL, null=True,)
    description = models.TextField(max_length=1000)
    daily_goal = models.TextField(max_length=1000, default="goal",)
    slug = models.SlugField(null=False, unique=True)

    def __str__(self):
        return f'{self.habit}'


class Tracker(models.Model):
    person = models.ForeignKey('User', on_delete=models.SET_NULL, null=True,)
    habit_tracked = models.ForeignKey(
        'Habit', on_delete=models.SET_NULL, null=True,)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.person}'


# Create your models here.
