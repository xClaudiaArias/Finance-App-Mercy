from django.forms import ModelForm
from dashboard.models import Users

class UserForm(ModelForm):
  class Meta:
    model = Users
    fields = ["username", "password"]
    
form = UserForm()

