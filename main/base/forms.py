from django import forms

class LoginPage(forms.Form):
    email = forms.EmailField(max_length=200)
    password = forms.CharField(max_length=200)


class RegisterPage(forms.Form):
    name = forms.CharField(max_length=200)
    email = forms.EmailField(max_length=200)
    password = forms.CharField(max_length=200)

