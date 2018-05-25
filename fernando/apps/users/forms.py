from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from .models import User, Profile_Client, Profile_Employee, Profile_Provider
from django import forms

class UserCreationForm(UserCreationForm):

	CLIENT = 1
	EMPLOYEE = 2
	PROVIDER = 3
	ADMIN = 4
	VISITOR = 5
	USER_TYPES = (
		(CLIENT, 'Client'),
        (EMPLOYEE, 'Employee'),
        (PROVIDER, 'Provider'),
        (ADMIN,'Admin'),
        (VISITOR,'Visitor')
        )

	user_type = forms.ChoiceField(choices = USER_TYPES, label=" User Type", initial='', widget=forms.Select(), required=True)
	

	class Meta:
		model = User
		fields = ('email','is_active',)