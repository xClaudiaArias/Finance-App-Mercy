from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

app_name = "dashboard"

urlpatterns = [
    path('', views.index, name="index"),
    path('accounts/', views.loginForm, name="loginForm"),
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('register/', views.register, name="register"),
    # path("")
    # path('test/', views.authUser, name="test")
    # path("your-name/", views.printname, name="your-name"),
    # path("form2/", views.getName, name="form2"),
    # path("form3/", views.getUserForm, name="form3")
]