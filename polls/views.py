from django.shortcuts import render, redirect, get_object_or_404, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from .models import User, Habit, Tracker
from .forms import HabitForm

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


def create_habit(request, pk):
    if request.method == 'POST':
        form = HabitForm(request.POST)
        if form.is_valid():
            return HttpResponseRedirect('/thanks/', pk=pk)
    else:
        form = HabitForm()
    return render(request, 'new_habit.html', {'form': form, 'pk': pk})
