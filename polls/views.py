from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import User, Habit, Tracker


# @login_required
def index(request):
    users = User.objects.all()
    return render(request, "core/index.html", {'users': users})


def daily_log(request):
    pass


def show_habits(request):
    habits = Habit.objects.all()
    return render(request, "core/tracker.html", {'habits': habits})

                  

def tracker(request):
    tracker = Tracker.objects.all()
    return render(request, )