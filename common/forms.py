from django.contrib.auth.forms import UserCreationForm
from django import forms


class RegisterForm(UserCreationForm):
    company_name = forms.CharField(max_length=200, required=True)
    company_address = forms.CharField(max_length=300, required=True)
