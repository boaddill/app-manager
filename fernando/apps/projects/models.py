from django.db import models
from django.db.models.signals import post_save,post_delete
from django.dispatch import receiver


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
	
#presupuestos
class Scope (models.Model):
	code            = models.CharField("Code", max_length=200, blank=True,null=True )
	project         = models.OneToOneField(Project, on_delete=models.CASCADE ,verbose_name="Project")
	date            = models.DateField("Date", max_length=200, blank=True,null=True )
	valid_until     = models.DateField('Valid untill',blank=True,null=True)
	total_price     = models.DecimalField(blank=True,null=True,decimal_places=2,max_digits=10)

	
#signal 
@receiver(post_save, sender=Project)
def create_scope(sender, instance, created, **kwargs):
	if created:
		Scope.objects.create( project=instance )
	else:
		pass

@receiver(post_save, sender=Project)
def save_scope(sender, instance,**kwargs):
    instance.scope.save()


#fases del proyecto
class Phase(models.Model):
	phase_code        = models.IntegerField( )
	phase_name        = models.CharField('Phase name ',max_length=200, blank=True,null=True)
	coments           = models.TextField("coments", max_length=400, blank=True,null=True,default='coments' )
	start_date        = models.DateField(blank=True, null=True)
	end_date          = models.DateField(blank=True, null=True)

	def __str__(self):
		return self.phase_name




#capitulos del proyecto
class Chapter (models.Model):
	code              = models.CharField("Code", max_length=200, blank=True,null=True )
	chapter_name      = models.CharField("Chapter name ", max_length=200, blank=True,null=True )
	quantity		  = models.DecimalField(blank=True,decimal_places=2,null=True,max_digits=10)
	total_price       = models.DecimalField(blank=True,null=True ,decimal_places=2,max_digits=10)
	scope    	      = models.ForeignKey(Scope,on_delete=models.CASCADE ,blank=True,null=True , verbose_name='Scope')
	

#partidas del proyecto

class Task (models.Model):
	code                 = models.CharField("Code", max_length=200, blank=True,null=True )
	task_name            = models.CharField("Task name ", max_length=200, blank=True,null=True )
	
	description          = models.TextField("coments", max_length=400, blank=True,null=True,default='coments')
	
	def __str__(self):
		return   self.task_name

class Project_Price(models.Model):
	task                = models.OneToOneField(Task, on_delete=models.CASCADE ,verbose_name="task")
	project             = models.OneToOneField(Project, on_delete=models.CASCADE ,verbose_name="Project")
	scope_price         = models.DecimalField(blank=True,decimal_places=2,null=True,max_digits=20)
	invoice_price       = models.DecimalField(blank=True,decimal_places=2,null=True,max_digits=20)
	planification_price = models.DecimalField(blank=True,decimal_places=2,null=True,max_digits=20)
	target_price        = models.DecimalField(blank=True,decimal_places=2,null=True,max_digits=20)

	class Meta:        
		verbose_name = "Project Price"
		verbose_name_plural = "Project Prices"

	def __str__(self):
		return   self.scope_price









# classes para las mediciones del presupuesto , objetivo , certificacion  y planificacion

class Scope_Meassurement(models.Model):

	task                = models.ForeignKey(Task, on_delete=models.CASCADE ,verbose_name="task")
	ud_type             = models.CharField("unidades", max_length=200, blank=True,null=True )
	quantity			= models.DecimalField(blank=True,decimal_places=2,null=True,max_digits=20)
	width		        = models.DecimalField(blank=True,decimal_places=2,null=True,max_digits=20)
	high    		    = models.DecimalField(blank=True,decimal_places=2,null=True,max_digits=20)
	wide    		    = models.DecimalField(blank=True,decimal_places=2,null=True,max_digits=20)
	total_meassurement  = models.DecimalField(blank=True,decimal_places=2,null=True,max_digits=20)
	phase               = models.ForeignKey(Phase,on_delete=models.CASCADE ,blank=True,null=True , verbose_name='phase')

	class Meta:        
		verbose_name = "Scope Meassurement"
		verbose_name_plural = "Scope Meassurements"

	def save(self):
		A=[]
		B=[self.width,self.high,self.wide]
		for i in B:
			if i!=None:
				A.append(i)
		C=1
		for i in A:
			C=C*i
		if self.quantity:
			self.total_meassurement=self.quantity*C
		else:
			self.total_meassurement=0
		return super(Scope_Meassurement,self).save()

#

		
class Invoice_Meassurement(models.Model):

	task                = models.ForeignKey(Task, on_delete=models.CASCADE ,verbose_name="task")
	ud_type             = models.CharField("unidades", max_length=200, blank=True,null=True )
	quantity			= models.DecimalField(blank=True,decimal_places=2,null=True,max_digits=20)
	width		        = models.DecimalField(blank=True,decimal_places=2,null=True,max_digits=20)
	high    		    = models.DecimalField(blank=True,decimal_places=2,null=True,max_digits=20)
	wide    		    = models.DecimalField(blank=True,decimal_places=2,null=True,max_digits=20)
	total_meassurement  = models.DecimalField(blank=True,decimal_places=2,null=True,max_digits=20)
	phase               = models.ForeignKey(Phase,on_delete=models.CASCADE ,blank=True,null=True , verbose_name='phase')

	class Meta:        
		verbose_name = "Invoice Meassurement"
		verbose_name_plural = "invoice Meassurements"



	def save(self):
		A=[]
		B=[self.width,self.high,self.wide]
		for i in B:
			if i!=None:
				A.append(i)
		C=1
		for i in A:
			C=C*i
		if self.quantity:
			self.total_meassurement=self.quantity*C
		else:
			self.total_meassurement=0
		return super(Invoice_Meassurement,self).save()



class Planification_Meassurement(models.Model):

	task                = models.ForeignKey(Task, on_delete=models.CASCADE ,verbose_name="task")
	ud_type             = models.CharField("unidades", max_length=200, blank=True,null=True )
	quantity			= models.DecimalField(blank=True,decimal_places=2,null=True,max_digits=20)
	width		        = models.DecimalField(blank=True,decimal_places=2,null=True,max_digits=20)
	high    		    = models.DecimalField(blank=True,decimal_places=2,null=True,max_digits=20)
	wide    		    = models.DecimalField(blank=True,decimal_places=2,null=True,max_digits=20)
	total_meassurement  = models.DecimalField(blank=True,decimal_places=2,null=True,max_digits=20)
	phase               = models.ForeignKey(Phase,on_delete=models.CASCADE ,blank=True,null=True , verbose_name='phase')

	class Meta:        
		verbose_name = "Planification Meassurement"
		verbose_name_plural = "Planification Meassurements"



	def save(self):
		A=[]
		B=[self.width,self.high,self.wide]
		for i in B:
			if i!=None:
				A.append(i)
		C=1
		for i in A:
			C=C*i
		if self.quantity:
			self.total_meassurement=self.quantity*C
		else:
			self.total_meassurement=0
		return super(Planification_Meassurement,self).save()

class Target_Meassurement(models.Model):

	task                = models.ForeignKey(Task, on_delete=models.CASCADE ,verbose_name="task")
	ud_type             = models.CharField("unidades", max_length=200, blank=True,null=True )
	quantity			= models.DecimalField(blank=True,decimal_places=2,null=True,max_digits=20)
	width		        = models.DecimalField(blank=True,decimal_places=2,null=True,max_digits=20)
	high    		    = models.DecimalField(blank=True,decimal_places=2,null=True,max_digits=20)
	wide    		    = models.DecimalField(blank=True,decimal_places=2,null=True,max_digits=20)
	total_meassurement  = models.DecimalField(blank=True,decimal_places=2,null=True,max_digits=20)
	phase               = models.ForeignKey(Phase,on_delete=models.CASCADE ,blank=True,null=True , verbose_name='phase')

	class Meta:        
		verbose_name = "Target Meassurement"
		verbose_name_plural = "Target Meassurements"



	def save(self):
		A=[]
		B=[self.width,self.high,self.wide]
		for i in B:
			if i!=None:
				A.append(i)
		C=1
		for i in A:
			C=C*i
		if self.quantity:
			self.total_meassurement=self.quantity*C
		else:
			self.total_meassurement=0
		return super(Target_Meassurement,self).save()		

#senal para creacion automatica de sets de mediciones cuando creamos una partida 

@receiver(post_save, sender=Task)
def create_meassurments(sender, instance, created, **kwargs):
	
	if created:
		ojb=Invoice_Meassurement(task=instance)
		ojb1=Scope_Meassurement(task=instance)
		ojb2=Planification_Meassurement(task=instance)
		ojb3=Target_Meassurement(task=instance)
		ojb4=Project_Price(task=instance)
		ojb.save()
		ojb1.save()
		ojb2.save()
		ojb3.save()
		ojb4.save()

		





	


	


	

	