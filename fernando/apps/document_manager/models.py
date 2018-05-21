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
	document_number  = models.CharField(max_length=30, blank=True,null=True ,verbose_name="Document number" )
	file             = models.FileField( upload_to='documents/' )
	uploaded_at      = models.DateTimeField( auto_now_add=True ) 
	uploaded_by      = models.ForeignKey(User,on_delete=models.CASCADE, verbose_name="uploader")
	project          = models.ForeignKey(Project,on_delete=models.CASCADE, blank=True,null=True ,verbose_name="Project")
	document_type    = models.ForeignKey(Document_Type,on_delete=models.CASCADE, blank=True,null=True ,verbose_name="Document type")



	
	
    


