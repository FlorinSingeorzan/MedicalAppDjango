from django.contrib.auth.models import User
from .models import Message
from django import forms


class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['first_name','last_name','email','username','password']


class MessageForm(forms.ModelForm):
    class Meta:
        model = Message
        fields = ['message', 'date', 'receiver']

