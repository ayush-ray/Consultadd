from django.urls import path

from . import views

app_name = "login"

urlpatterns = [
    path('', views.login, name='login'),
    path('home/', views.home_view, name='home'),
    path('register/', views.register, name='register'),
]