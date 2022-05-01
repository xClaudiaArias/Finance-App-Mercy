from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Users

class RegisterUser(UserCreationForm):
  class Meta:
    db_table = 'Users'
    model = User
    fields = ("first_name", "last_name", "username", "email")
    

registerForm = RegisterUser()
if registerForm.is_valid():
  newUser = registerForm.save()
  