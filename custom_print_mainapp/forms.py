from django import forms
from .models import reg_donor_patient,add_reqdonate, add_reqblood
from django.contrib.auth.models import User
from django.contrib.auth.forms import PasswordChangeForm, UserCreationForm


class register(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email','password1','password2','first_name','last_name']