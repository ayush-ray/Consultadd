from django.urls import path
from django.contrib import admin

from . import views

app_name = "ecommerce"

urlpatterns = [
    path('', views.index,name="index"),
]
