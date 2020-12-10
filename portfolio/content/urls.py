from django.contrib import admin
from django.urls import path
from . import views

app_name='content'

urlpatterns = [
    path('', views.content_index, name='landing'),
]
