from django import forms
from django.contrib.auth import authenticate
from django.contrib.auth.forms import (UserCreationForm, AuthenticationForm)
from django.contrib.auth.models import User
from django.forms import fields


class CreateUserForm(UserCreationForm):
    class Meta():
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class LoginUserForm(AuthenticationForm):
    class Meta():
        model = User
        fields = ['username', 'password']
    
    # def clean(self):
    #     if self.is_valid():
    #         username = self.cleaned_data['username']
    #         password = self.cleaned_data['password']
    #         # Raise authentication error
    #         if not authenticate(email=username, password=password):
    #             raise forms.ValidationError("Invalid Credentials! Please insert correct email & password.")