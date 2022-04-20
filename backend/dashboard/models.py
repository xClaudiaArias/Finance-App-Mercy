from datetime import datetime
from tkinter import CASCADE
from django.db import models
from django.utils import timezone

# Create your models here.
class User(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    username = models.CharField(max_length=15)
    email = models.CharField(max_length=25)
    password = models.CharField(max_length=15)
    created_at = timezone.now()
    
class Bills(models.Model):
    user = models.ForeignKey(User, default=1, on_delete=models.CASCADE)
    rent_mortgage = models.DecimalField(max_digits=10, decimal_places=2)
    gas = models.DecimalField(max_digits=10, decimal_places=2)
    electrical = models.DecimalField(max_digits=10, decimal_places=2)
    mobile = models.DecimalField(max_digits=10, decimal_places=2)
    cable = models.DecimalField(max_digits=10, decimal_places=2)
    transportation = models.DecimalField(max_digits=10, decimal_places=2)
    car = models.DecimalField(max_digits=10, decimal_places=2)
    groceries = models.DecimalField(max_digits=10, decimal_places=2)
    education = models.DecimalField(max_digits=10, decimal_places=2)
    
class Expenses(models.Model):
    user = models.ForeignKey(User, default=1, on_delete=models.CASCADE)
    takeout = models.DecimalField(max_digits=10, decimal_places=2)
    concert = models.DecimalField(max_digits=10, decimal_places=2)
    shopping = models.DecimalField(max_digits=10, decimal_places=2)
    
class Income(models.Model):
    user = models.ForeignKey(User, default=1, on_delete=models.CASCADE)
    job1 = models.DecimalField(max_digits=10, decimal_places=2)

class Balance(models.Model):
    user = models.ForeignKey(User, default=1, on_delete=models.CASCADE)
    income = models.ForeignKey(Income, default=1, on_delete=models.CASCADE)
    expenses = models.ForeignKey(Expenses, default=1, on_delete=models.CASCADE)
    date = models.DateField()
    updated_at = timezone.now()
    # difference = models.DecimalField(max_digits=10, decimal_places=2)
    
class Savings(models.Model):
    user = models.ForeignKey(User, default=1, on_delete=models.CASCADE)
    balance = models.ForeignKey(Balance, default=1, on_delete=models.CASCADE)
    income = models.ForeignKey(Income, default=1, on_delete=models.CASCADE)
    deposit = models.DecimalField(max_digits=10, decimal_places=2)
    total_amount = models.DecimalField(max_digits=10, decimal_places=2)
    updated_at = timezone.now()
    
class Budget(models.Model):
    user = models.ForeignKey(User, default=1, on_delete=models.CASCADE)
    updated_at = timezone.now()
    transportation = models.DecimalField(max_digits=10, decimal_places=2)
    groceries = models.DecimalField(max_digits=10, decimal_places=2)
    
class Goals(models.Model):
    user = models.ForeignKey(User, default=1, on_delete=models.CASCADE)
    updated_at = timezone.now()
    travel = models.DecimalField(max_digits=10, decimal_places=2)
    buy_house = models.DecimalField(max_digits=10, decimal_places=2)