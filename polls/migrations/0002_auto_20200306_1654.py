# Generated by Django 3.0.4 on 2020-03-06 16:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='habit',
            old_name='habit_user',
            new_name='user',
        ),
        migrations.AlterField(
            model_name='habit',
            name='daily_goal',
            field=models.TextField(default='goal', max_length=200),
        ),
        migrations.AlterField(
            model_name='habit',
            name='description',
            field=models.TextField(max_length=500),
        ),
    ]
