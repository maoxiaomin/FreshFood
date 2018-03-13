from django import forms

class RegisterForm(forms.Form):
    username = forms.CharField(min_length=4, max_length=20)
    pwd = forms.CharField(min_length=4, max_length=20)
    cpwd = forms.CharField(min_length=4, max_length=20)
    email = forms.EmailField()
    allow = forms.BooleanField()

class LoginForm(forms.Form):
    username = forms.CharField(min_length=4, max_length=20)
    pwd = forms.CharField(min_length=4, max_length=20)