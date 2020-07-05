from django.urls import path
from blog import views

app_name = "blog"

urlpatterns = [
    path('create', views.blogging, name="create"),
    path('show', views.show, name="showall"),
    path('update/<int:id>', views.update, name="update"),
    path('delete/<int:id>', views.destroy, name="delete"),
]
