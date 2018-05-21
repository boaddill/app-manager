from django import forms
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from apps.user.models import User, Profile_Client, Profile_Employee, Profile_Provider



class Profile_Client_Form(ModelForm):
    class Meta:
        model = Profile_Client
        exclude  = ['user']

class Profile_Employee_Form(ModelForm):
    class Meta:
        model = Profile_Employee
        exclude  = ['user']


class Profile_Provider_Form(ModelForm):
    class Meta:
        model = Profile_Provider
        exclude  = ['user']