from django.db import models


class Project(models.Model):
	"""docstring for invoice:"""

	ACCEPTED='ACT'
	WAITING = 'WFA'
	OVERRULLED= 'REJ'
	STATE_TYPES = (
		(ACCEPTED, 'Accepted'),
        (WAITING, 'Waiting'),
        (OVERRULLED, 'Provider'),
        
        )


	project_name    = models.CharField(max_length=200, blank=True, null=True)
	project_number  = models.CharField(max_length=200, blank=True)
	project_address = models.CharField(max_length=200, blank=True,null=True)
	start_date      = models.DateField(blank=True, null=True)
	end_date        = models.DateField(blank=True, null=True)
	project_manager = models.ForeignKey('users.Profile_Employee',on_delete=models.CASCADE, blank=True,null=True ,verbose_name="Project manager",related_name='project_manager')
	work_force      = models.ManyToManyField('users.Profile_Employee', blank=True,verbose_name="Resources",related_name="work_force")
	client          = models.ForeignKey('users.Profile_client',on_delete=models.CASCADE,null=True ,blank=True,verbose_name="client",related_name="client")
	state           = models.CharField(max_length=3, choices = STATE_TYPES,default=WAITING)
	
	def __str__(self):
		return   self.project_name

	

	