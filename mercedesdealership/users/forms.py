from django import forms
from .models import Profile
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.core.validators import RegexValidator

class UserRegisterForm(UserCreationForm):
    phone_regex = RegexValidator(regex=r"^\+?1?\d{8,15}$")
    email=forms.EmailField(max_length=100,required=True)
    first_name=forms.CharField(max_length=100,required=True)
    last_name=forms.CharField(max_length=100,required=True)
    phone=forms.CharField(validators=[phone_regex],required=True)
    city=forms.CharField(max_length=50,required=True)
    class Meta:
        model=User
        fields=["username","email","first_name","last_name","phone","city","password1","password2"]

class EditForm(forms.ModelForm):
    email = forms.EmailField(max_length=100, required=True)
    first_name = forms.CharField(max_length=100, required=True)
    last_name = forms.CharField(max_length=100, required=True)
    class Meta:
        model=User
        fields=["email","first_name","last_name"]

class EditProfileForm(forms.ModelForm):
    phone_regex = RegexValidator(regex=r"^\+?1?\d{8,15}$")
    phone_number = forms.CharField(validators=[phone_regex], required=True)
    city = forms.CharField(max_length=50, required=True)
    class Meta:
        model=User
        fields=["phone_number","city"]