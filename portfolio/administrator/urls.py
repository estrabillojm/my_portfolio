from django.contrib import admin
from django.urls import path
from . import views

app_name='a_panel'

urlpatterns = [
    path('', views.admin_login, name='login'),
]
