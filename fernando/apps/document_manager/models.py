from django.db import models
from apps.users.models import User
from apps.projects.models import Project


class Document_Type(models.Model):

	DRAWING='DRG'
	IMAGEN='IMG'
	QUOTE='QOT'
	INVOICE='INV'
	ENGINEER='ENG'

	document_type=(
		(DRAWING,'Drawing'),
		(IMAGEN,'Imagen'),
		(QUOTE,'Quote'),
		(INVOICE,'Ivoice'),
		(ENGINEER,'Egineer')
		)

	
	type   = models.CharField(choices=document_type ,default=IMAGEN, max_length=32, blank=True, )






class File(models.Model):
	pass

	
	
    


