from datetime import datetime
from pyexpat import model
from tkinter import CASCADE
from unicodedata import category
from django.db import models
from django.utils import timezone
from django import forms

# Create your models here.
class User(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    username = models.CharField(max_length=15)
    email = models.EmailField(max_length=50)
    password = models.CharField(max_length=15)
    created_at = timezone.now()

class Transaction(models.Model):
    user = models.ForeignKey(User, default=1, on_delete=models.CASCADE)
    category = models.CharField(max_length=30)
    transc_name = models.CharField(max_length=30)
    transaction_date = timezone.now()
    amount_paid = models.DecimalField(default=0, max_digits=10, decimal_places=2)
    
class Bills(models.Model):
    user = models.ForeignKey(User, default=1, on_delete=models.CASCADE)
    transaction = models.ForeignKey(Transaction, default=1, on_delete=models.CASCADE)
    amount_due = models.DecimalField(default=0, max_digits=10, decimal_places=2)
    due_date = forms.DateField()
    isPaid = models.BooleanField(default=True)
    pay_date = forms.DateField()
    
class Budget(models.Model):
    user = models.ForeignKey(User, default=1, on_delete=models.CASCADE)
    transaction = models.ForeignKey(Transaction, default=1, on_delete=models.CASCADE)
    category = models.CharField(max_length=30, default="Caterogy")
    budget_goal = models.DecimalField(default=0, max_digits=10, decimal_places=2)
    created_at = timezone.now()

class Income(models.Model):
    user = models.ForeignKey(User, default=1, on_delete=models.CASCADE)
    income_name = models.CharField(max_length=20, default="income_name")
    created_at = timezone.now()
    deposit = models.DecimalField(default=0, max_digits=10, decimal_places=2)
    total_amount = models.DecimalField(default=0, max_digits=10, decimal_places=2)
    updated_at = models.DateTimeField('updated_at', auto_now=True)

class Balance(models.Model):
    user = models.ForeignKey(User, default=1, on_delete=models.CASCADE)
    income = models.ForeignKey(Income, on_delete=models.CASCADE)
    transaction = models.ForeignKey(Transaction, default=0, on_delete=models.CASCADE)
    date = models.DateField()
    updated_at = timezone.now()
    difference = models.DecimalField(default=0, max_digits=10, decimal_places=2)
    
class Savings(models.Model):
    user = models.ForeignKey(User, default=1, on_delete=models.CASCADE)
    transaction = models.ForeignKey(Transaction, default=1, on_delete=models.CASCADE)
    income = models.ForeignKey(Income, default=0, on_delete=models.CASCADE)
    deposit_amount = models.DecimalField(default=0, max_digits=10, decimal_places=2)
    total_amount = models.DecimalField(default=0, max_digits=10, decimal_places=2)
    updated_at = timezone.now()
    
class Goals(models.Model):
    user = models.ForeignKey(User, default=1, on_delete=models.CASCADE)
    category = models.CharField(max_length=30, default="category")
    updated_at = timezone.now()
    goal_name = models.CharField(max_length=30, default="goal_name")
    amount_to_save = models.DecimalField(default=0, max_digits=10, decimal_places=2)
    amount_saved = models.DecimalField(default=0, max_digits=10, decimal_places=2)