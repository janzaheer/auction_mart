from django.contrib.auth import password_validation
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django import forms


class LoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'autofocus': True, 'class': 'border p-3 w-100 my-2'}))
    password = forms.CharField(
        label="Password",
        strip=False,
        widget=forms.PasswordInput(attrs={'autocomplete': 'current-password', 'class': 'border p-3 w-100 my-2'}),
    )


class RegisterForm(UserCreationForm):
    username = forms.CharField(max_length=200, required=True,
                               widget=forms.TextInput(attrs={'class': 'border p-3 w-100 my-2'}))
    password1 = forms.CharField(
        label="Password",
        strip=False,
        widget=forms.PasswordInput(attrs={'autocomplete': 'new-password', 'class': 'border p-3 w-100 my-2'}),
        help_text=password_validation.password_validators_help_text_html(),
    )
    password2 = forms.CharField(
        label="Password confirmation",
        widget=forms.PasswordInput(attrs={'autocomplete': 'new-password', 'class': 'border p-3 w-100 my-2'}),
        strip=False,
        help_text="Enter the same password as before, for verification.",
    )
    company_name = forms.CharField(max_length=200, required=True,
                                   widget=forms.TextInput(attrs={'class': 'border p-3 w-100 my-2'}))
    company_address = forms.CharField(max_length=300, required=True,
                                      widget=forms.TextInput(attrs={'class': 'border p-3 w-100 my-2'}))
