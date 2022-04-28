from django.forms import ModelForm
from dashboard.models import User

class UserForm(ModelForm):
  class Meta:
    model = User
    fields = ["first_name", "last_name", "username", "email", "password"]
    
# form3 = UserForm()
# if form3.is_valid():
#   newUser = form3.save()
  
  
# user1 = UserForm.objects.get(pk='1')
# form = UserForm(instance=user1)
