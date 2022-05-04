from django.forms import ModelForm
from dashboard.models import Income
from dataclasses import field
from django import forms
from django.db import models

class AddIncome(ModelForm):
    class Meta:
      db_table = 'dashboard_income'
      model = Income
      fields = ["income_name", "deposit"]
      
    def save(self, commit=True):
      income = super(AddIncome, self).save(commit=False)
      income.income_name = self.cleaned_data['income_name']
      income.deposit = self.cleaned_data['deposit']

      if commit:
          income.save()

      return income
    
add_income_form = AddIncome()


