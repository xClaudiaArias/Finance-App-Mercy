from django import forms

class NameForm(forms.Form):
  your_name = forms.CharField(label='form2', max_length=100)