from django.forms import ModelForm
from dashboard.models import User

class UserForm(ModelForm):
  class Meta:
    model = User
    fields = ["username", "password"]
    
form3 = UserForm()

# if form3.is_valid():
#   newUser = form3.save()
  