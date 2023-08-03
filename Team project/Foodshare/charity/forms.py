from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms
from .models import Donations

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        
class Form(forms.ModelForm):
  class Meta:
    model = Donations
    fields = ["donor_name", "donor_mobile", 'donor_email',  'Donation_type', 'quantity' ]
    labels = {'donor_name': "Name", "donor_mobile": "Mobile Number", 'donor_email': 'donor_email', 'type':'Donation_type', 'quantity': 'quantity'}        