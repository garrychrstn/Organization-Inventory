from django.contrib import admin
from django.urls import path, include
from . import views
from django.contrib.auth import views as auth_views

app_name = 'main'

urlpatterns = [
    path('', views.index, name='index'),
    path('add-event', views.addEvent, name='addE'),
    path('add-item', views.addItems, name='addI'),
    path('login', views.login_request, name='login'),
    path('add-member', views.addMembers, name='addM'),
    path('display-item', views.displayItems, name='displayItems'),
]