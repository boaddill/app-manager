from django.forms import ModelForm
from django import forms
from .models import *
from fernando import settings



class Project_Creation_Form(ModelForm):


	
	class Meta:
		model = Project
		fields = '__all__'



class Entry_Creation_Form(ModelForm):

	class Meta:
		model = Entry
		fields = '__all__'


class Chapter_Creation_Form(ModelForm):

	class Meta:
		model = Chapter
		fields = ('code','units','chapter_name','quantity_scope','quantity_invoice','quantity_planif','quantity_target','quantity_real')

class Meassurement_Creation_Form(ModelForm):

	class Meta:
		model =  Scope_Meassurement
		exclude = ('entry ','total_meassurement', 'indirect_cost_entry',)


class Entry_Item_Price_Form (ModelForm) :

	model  =  Entry_Item_Price
	fields =  ('item', 'quantity_per_entry_unit_scope', 'item_price',)



