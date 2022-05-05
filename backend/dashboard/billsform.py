from django.forms import ModelForm
from dashboard.models import Bills
from dataclasses import field
from django import forms
from django.db import models

class AddBill(ModelForm):
    due_date =  forms.DateField(input_formats='%m/%d/%Y')
    pay_date = forms.DateField(input_formats='%m/%d/%Y')
    
    class Meta:
      db_table = 'dashboard_income'
      model = Bills
      fields = ["category", "bill_name", "amount_due", "isPaid", "pay_date"]
      
    def save(self, commit=True):
      bill = super(AddBill, self).save(commit=False)
      bill.category = self.cleaned_data['category']
      bill.bill_name = self.cleaned_data['bill_name']
      bill.deposit = self.cleaned_data['deposit']
      bill.amount_due = self.cleaned_data['amount_due']

      if commit:
          bill.save()

      return bill
    
add_bill = AddBill()


