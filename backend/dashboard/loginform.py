from django.forms import ModelForm
from dashboard.models import Users

class UserForm(ModelForm):
  class Meta:
    model = Users
    fields = ["username", "password"]
    
form3 = UserForm()

# if form3.is_valid():
#   newUser = form3.save()
  