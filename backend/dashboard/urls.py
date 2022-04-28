from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("your-name/", views.printname, name="your-name"),
    path("form2/", views.getName, name="form2"),
    path("form3/", views.getUserForm, name="form3")
]