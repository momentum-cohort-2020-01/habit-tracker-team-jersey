from django.shortcuts import render

from .models import User, Habit, Tracker

from django.contrib.auth.decorators import login_required


@login_required
def index(request):
    users = User.objects.all()
    return render(request, "config/habit_list.html", {'habits': habits})


def daily_log(request):
    pass


def show_habits(request):
    habit = Habit.objects.all()
    return render(request, "config/habit_choices.html", {'habits': habits})

                  

def tracker(request):
    tracker = Tracker.objects.all()
    return render(request, )