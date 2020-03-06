"""core URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from polls import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', views.index, name="home"),
    path('habit-tracker/<int:pk>', views.tracker, name='habit-tracker'),
    path('create-habit/', views.create_habit, name='create-habit'),
    path('edit-habit/<int:pk>', views.edit_habit, name='edit-habit'),
    path('delete-habit/', views.delete_habit, name='delete-habit'),
    path('admin/', admin.site.urls),


# __debug__/
# [name='home']
# habit-tracker/<int:pk> [name='habit-tracker']
# create-habit/ [name='create-habit']
# todos/<int:pk>/edit/ [name='habit-edit']
# todos/<int:pk>/delete/ [name='habit-delete']
# admin/



# From the website https://django-debug-toolbar.readthedocs.io/en/latest/installation.html and her example from class.
if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [
        path('__debug__/', include(debug_toolbar.urls)),

        # For django versions before 2.0:
        # url(r'^__debug__/', include(debug_toolbar.urls)),

    ] + urlpatterns
