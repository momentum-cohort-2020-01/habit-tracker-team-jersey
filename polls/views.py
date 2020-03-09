from django.shortcuts import render, redirect, get_object_or_404, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from .models import User, Habit, Tracker
from .forms import HabitForm, ProgressForm
from django.contrib.auth import authenticate, login


def my_view(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(username=username, password=password)
    if user is not None:
        if user.is_active:
            login(request, user)
            redirect("home")
        else:
            return render("Account is not active")
            ...
    else:
        return render('Nope. Invalid Login Credentials')

# @login


def index(request):
    users = User.objects.all()
    habits = Habit.objects.order_by('-updated_at')
    logs = Tracker.objects.all()
    # last_logged_habit = Tracker.objects.filter('updated_at').order_by('-id')[0]
    # last_logged_value = Tracker.objects.filter(input_units).order_by('-id')[0]

    return render(request, "core/index.html", {'users': users, "habits": habits, "logs": logs})


# def show_habits(request):
#     habits = Habit.objects.all()
#     return render(request, "core/tracker.html", {'habits': habits})


def log(request, pk):
    form = get_object_or_404(Tracker, pk=pk)
    if request.method == 'POST':
        form = ProgressForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("home")
    else:
        form = ProgressForm()
    return render(request, 'core/log.html', {'form': form})


def log_record(request, pk):
    logs = Tracker.objects.all()
    habit = get_object_or_404(Habit, pk=pk)
    return render(request, 'core/log_record.html', {'logs': logs, 'habit': habit})


def create_habit(request):
    if request.method == 'POST':
        form = HabitForm(request.POST)
        if form.is_valid():
            habit = form.save()
            return redirect("home")
    else:
        form = HabitForm()
    return render(request, 'core/create_habit.html', {'form': form})


def edit_habit(request, pk):
    habit = get_object_or_404(Habit, pk=pk)

    if request.method == 'POST':
        form = HabitForm(request.POST, instance=habit)
        if form.is_valid():
            form.save()

            return redirect('home')
    else:
        form = HabitForm(instance=habit)

    return render(request, 'core/edit_habit.html', {"form": form})


def delete_habit(request, pk):
    habit = get_object_or_404(Habit, pk=pk)
    habit.delete()
    return redirect('home')
