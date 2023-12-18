# main/forms.py

from django import forms


class InsecureForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)
