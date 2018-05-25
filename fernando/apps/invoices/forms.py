from django.forms import ModelForm
from .models import Item
from django import forms

class ItemCreationForm(UserCreationForm):

	

	class Meta:
		model = User
		fields = ('__all__')