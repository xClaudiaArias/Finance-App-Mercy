from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("your-name/", views.printname, name="your-name")
]