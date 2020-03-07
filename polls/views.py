from django.shortcuts import render, redirect, get_object_or_404, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from .models import User, Habit, Tracker
from .forms import HabitForm


# @login_required
def index(request):
    users = User.objects.all()
    habits = Habit.objects.order_by('-created_at')
    return render(request, "core/index.html", {'users': users, "habits": habits})


def daily_log(request):
    pass


# def show_habits(request):
#     habits = Habit.objects.all()
#     return render(request, "core/tracker.html", {'habits': habits})


def tracker(request):
    tracker = Tracker.objects.all()
    return render(request, )


def create_habit(request):
    if request.method == 'POST':
        form = HabitForm(request.POST)
        if form.is_valid():
            habit = form.save()
            return redirect("home", pk=habit.pk)
    else:
        form = HabitForm()
    return render(request, 'core/create_habit.html', {'form': form})


def edit_habit(request, pk):
    habit = get_object_or_404(Habit, pk=pk)

    if request.method == 'POST':
        form = HabitForm(request.POST, instance=habit)
        if form.is_valid():
            form.save()

            return redirect('edit-habit', pk=habit.pk)
    else:
        form = HabitForm(instance=habit)

    return render(request, 'core/edit_habit.html', {"form": form})


def delete_habit(request, pk):
    habit = get_object_or_404(Habit, pk=pk)
    habit.delete()
    return redirect('home')


def log_progress(request, pk):
    pass
