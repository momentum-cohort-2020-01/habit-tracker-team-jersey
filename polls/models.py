from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify
from datetime import datetime

# The daily target


class User(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=254, unique=True)

    def __str__(self):
        return f'{self.name}'


class Habit(models.Model):
    habit_name = models.CharField(max_length=100)
    action = models.CharField(max_length=100)
    user = models.ForeignKey(
        'User', on_delete=models.SET_NULL, null=True,)
    description = models.TextField(max_length=500)
    goal = models.IntegerField(default="",)
    unit = models.CharField(max_length=20, default="",)
    timeframe = models.CharField(max_length=20, default="",)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    # slug = models.SlugField(max_length=60, null=False, unique=True,
    #                         default="")

    def __str__(self):
        return f'{self.habit_name}'

    # def save(self, *args, **kwargs):
    #     if not self.slug:
    #         slug = slugify(self.habit)
    #     return super().save(*args, **kwargs)


class Tracker(models.Model):
    person = models.ForeignKey(
        'User', related_name='user', on_delete=models.SET_NULL, null=True,)
    habit_tracked = models.ForeignKey(
        'Habit', related_name='habit', on_delete=models.SET_NULL, null=True,)
    updated_at = models.DateTimeField(auto_now=True)
    input_units = models.IntegerField()

    def __str__(self):
        return f'{self.person}{self.habit_tracked}{self.updated_at}{self.input_units}'


# Create your models here.
