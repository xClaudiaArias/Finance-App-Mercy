from dataclasses import field
from django import forms
from django.contrib.auth.forms import UserCreationForm, User as u
from django.contrib.auth.models import User
# from dashboard.models import Users 
from django.db import models

class RegisterUser(UserCreationForm):

  class Meta:
    db_table = 'dashboard_users'
    # model = Users
    model = User
    fields = ("first_name", "last_name", "username", "email")

  # def save(self, commit=True):
  #       user = super(RegisterUser, self).save(commit=False)
  #       user.email = self.cleaned_data['email']
  #       user.first_name = self.cleaned_data['first_name']
  #       user.last_name = self.cleaned_data['last_name']

  #       if commit:
  #           user.save()

  #       return user
    


  