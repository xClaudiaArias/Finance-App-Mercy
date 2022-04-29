from datetime import datetime
import datetime
from pyexpat import model
from tkinter import CASCADE
from unicodedata import category
from django.db import models
from django.utils import timezone
from django import forms
from django.contrib.auth.models import User

# Create your models here.

class Users(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    username = models.CharField(max_length=15)
    email = models.EmailField(max_length=50)
    password = models.CharField(max_length=15)
    created_at = timezone.now()
    
    
    # testing 
    def populateIndex():
        return 'Populate Index'
    
class Bills(models.Model):
    user = models.ForeignKey(Users, default=1, on_delete=models.CASCADE)
    category = models.CharField(max_length=30, default="category")
    bill_name = models.CharField(max_length=30, default="bill name")
    amount_due = models.DecimalField(default=0, max_digits=10, decimal_places=2)
    due_date = forms.DateField()
    isPaid = models.BooleanField(default=False)
    pay_date = forms.DateField()
    
    
# probably will have to delete bills from transaction 
# include category and all that locally 
class Transaction(models.Model):
    user = models.ForeignKey(Users, default=1, on_delete=models.CASCADE)
    category = models.CharField(max_length=30, default="category")
    bill_name = models.CharField(max_length=30, default="bill name")
    transaction_date = timezone.now()
    amount_paid = models.DecimalField(default=0, max_digits=10, decimal_places=2)
class Budget(models.Model):
    user = models.ForeignKey(Users, default=1, on_delete=models.CASCADE)
    category = models.CharField(max_length=30, default="Category")
    amount_saved = models.DecimalField(default=0, max_digits=10, decimal_places=2)
    budget_goal = models.DecimalField(default=0, max_digits=10, decimal_places=2)
    created_at = timezone.now()
    


class Income(models.Model):
    user = models.ForeignKey(Users, default=1, on_delete=models.CASCADE)
    income_name = models.CharField(max_length=20, default="income_name")
    created_at = timezone.now()
    deposit = models.DecimalField(default=0, max_digits=10, decimal_places=2)
    updated_at = models.DateTimeField('updated_at', auto_now=True)

class Balance(models.Model):
    user = models.ForeignKey(Users, default=1, on_delete=models.CASCADE)
    income = models.ForeignKey(Income, on_delete=models.CASCADE)
    transaction = models.ForeignKey(Transaction, default=0, on_delete=models.CASCADE)
    difference = models.DecimalField(default=0, max_digits=10, decimal_places=2)
    date_bal = models.DateTimeField('balance_date', auto_now=True)
    updated_at = timezone.now()
    
class Savings(models.Model):
    user = models.ForeignKey(Users, default=1, on_delete=models.CASCADE)
    transaction = models.ForeignKey(Transaction, default=1, on_delete=models.CASCADE)
    deposit_amount = models.DecimalField(default=0, max_digits=10, decimal_places=2)
    total_amount = models.DecimalField(default=0, max_digits=10, decimal_places=2)
    updated_at = timezone.now()
    
    
# maybe goals should reference transcations 
class Goals(models.Model):
    user = models.ForeignKey(Users, default=1, on_delete=models.CASCADE)
    goal_name = models.CharField(max_length=30, default="goal_name")
    amount_to_save = models.DecimalField(default=0, max_digits=10, decimal_places=2)
    amount_saved = models.DecimalField(default=0, max_digits=10, decimal_places=2)
    updated_at = timezone.now()