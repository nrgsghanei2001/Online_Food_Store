from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import *
from django.contrib.auth.models import User

# class CustomUserCreationForm(UserCreationForm):
#     class Meta(UserCreationForm): 
#         model = Customer 
#         # fields = UserCreationForm.Meta.fields + ('age',)
#         fields = ('email',)


class RegisterForm(UserCreationForm):
    email = forms.EmailField(max_length=100, required = True, help_text='Enter Email Address', widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Email'}),)
    username = forms.CharField(max_length=200, required = True, help_text='Enter Username', widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Username'}),)
    password1 = forms.CharField(help_text='Enter Password', required = True, widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Password'}),)
    password2 = forms.CharField(required = True,help_text='Enter Password Again',widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Password Again'}),)
    check = forms.BooleanField(required = True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2', 'check',]