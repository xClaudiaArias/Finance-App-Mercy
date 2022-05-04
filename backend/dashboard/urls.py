from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from django.views.generic import TemplateView

app_name = "dashboard"

urlpatterns = [
    path('', views.index, name="index"),
    path('accounts/', views.loginForm, name="loginForm"),
    path('login/', auth_views.LoginView.as_view(redirect_authenticated_user=True), name='login'),
    path('register/', views.register, name="register"),
    # path('accounts/profile/', TemplateView.as_view(template_name="dashboard/profile.html")),
    path('accounts/profile/', views.profile, name="profile"),
    # path('accounts/profile/', views.addIncomeForm, name="addIncomeForm")
    # path("")
    # path('test/', views.authUser, name="test")
    # path("your-name/", views.printname, name="your-name"),
    # path("form2/", views.getName, name="form2"),
    # path("form3/", views.getUserForm, name="form3")
]