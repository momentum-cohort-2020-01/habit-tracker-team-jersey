from django import forms
from .models import User, Habit, Tracker


class HabitForm(forms.ModelForm):

    class Meta:
        model = Habit
        fields = ('habit_name', 'action', 'goal', 'unit', 'timeframe')


class ProgressForm(forms.ModelForm):

    class Meta:
        model = Tracker
        fields = ('input_units',)
