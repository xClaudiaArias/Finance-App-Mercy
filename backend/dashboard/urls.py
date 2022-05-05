from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from django.views.generic import TemplateView
from dashboard.views import IncomeProfile
from dashboard.views import BillsProfile

app_name = "dashboard"

urlpatterns = [
    path('', views.index, name="index"),
    path('accounts/', views.loginForm, name="loginForm"),
    path('login/', auth_views.LoginView.as_view(redirect_authenticated_user=True), name='login'),
    path('register/', views.register, name="register"),
    # path('accounts/profile/', views.profile, name="profile"), # this will display all later. 
    path('accounts/profile/', views.IncomeProfile.as_view()), # this will display all later. 
    path('accounts/profile/1', views.BillsProfile.as_view()), # this will display all later. 
    # path('accounts/profile/income/', views.incomeForm, name="incomeForm"),
    # path('accounts/profile', showIncome.as_view(), name="show income")
]