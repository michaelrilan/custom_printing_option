from django import forms
from .models import print_options
from django.contrib.auth.models import User
from django.contrib.auth.forms import PasswordChangeForm, UserCreationForm


class print_option_form(forms.ModelForm):
    class Meta:
        model = print_options
        fields = ['print_name']