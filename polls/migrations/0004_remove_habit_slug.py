# Generated by Django 3.0.4 on 2020-03-07 21:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0003_auto_20200306_1903'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='habit',
            name='slug',
        ),
    ]