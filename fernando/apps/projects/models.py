from django.db import models
from django.db.models.signals import post_save,post_delete
from django.dispatch import receiver

class Project(models.Model):
	"""docstring for invoice:"""

	ACCEPTED='ACT'
	WAITING = 'WFA'
	OVERULLED= 'REJ'
	STATE_TYPES = (
		(ACCEPTED, 'Accepted'),
        (WAITING, 'Waiting'),
        (OVERULLED, 'Overruled'),
               )
	
	project_name    = models.CharField(max_length=200, blank=True, null=True)
	project_number  = models.CharField(max_length=200, blank=True)
	date            = models.DateField(blank=True, null=True)
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

	def __str__(self):
		return   self.project.project_name
	
	
#signal 
@receiver(post_save, sender=Project)
def create_scope(sender, instance, created, **kwargs):
	if created:
		Scope.objects.create( project=instance )
		print('hecho')

	else:
		pass

@receiver(post_save, sender=Project)
def save_scope(sender, instance,**kwargs):
    instance.scope.save()
    print('hola')
    


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
	code              = models.IntegerField( )
	chapter_name      = models.CharField("Chapter name ", max_length=200, blank=True,null=True )
	quantity		  = models.DecimalField(blank=True,decimal_places=2,null=True,max_digits=10)
	total_price       = models.DecimalField(blank=True,null=True ,decimal_places=2,max_digits=10)
	scope    	      = models.ForeignKey(Scope,on_delete=models.CASCADE ,blank=True,null=True , verbose_name='Scope')
	def __str__(self):
		return "%s - %s" %(self.chapter_name ,self.scope.project.project_name)
	

#partidas del proyecto


class Task (models.Model):
	code                 = models.CharField("Code", max_length=200, blank=True,null=True )
	task_name            = models.CharField("Task name ", max_length=200, blank=True,null=True )
	
	description          = models.TextField("coments", max_length=400, blank=True,null=True,default='coments')
	

class Entry (models.Model):

	entry_name            = models.CharField("Entry name ", max_length=200, blank=True,null=True )
	code                  = models.CharField("Code", max_length=200, blank=True,null=True )
	description           = models.TextField("Coments", max_length=400, blank=True,null=True,default='coments')
	items   	          = models.ManyToManyField('invoices.Item',blank=True,verbose_name="Items")
	chapter    	          = models.ForeignKey(Chapter,on_delete=models.CASCADE ,blank=True , verbose_name='Chapter - Project')
	scope_quantity		  = models.DecimalField(blank=True,decimal_places=2,null=True,max_digits=20)
	scope_unt_price		  = models.DecimalField(blank=True,decimal_places=2,null=True,max_digits=20)
	invoice_unt_price     = models.DecimalField(blank=True,decimal_places=2,null=True,max_digits=20)
	planif_unt_price      = models.DecimalField(blank=True,decimal_places=2,null=True,max_digits=20)
	target_unt_price      = models.DecimalField(blank=True,decimal_places=2,null=True,max_digits=20)
	scope_price		      = models.DecimalField(blank=True,decimal_places=2,null=True,max_digits=20)
	invoice_price         = models.DecimalField(blank=True,decimal_places=2,null=True,max_digits=20)
	planif_price          = models.DecimalField(blank=True,decimal_places=2,null=True,max_digits=20)
	target_price          = models.DecimalField(blank=True,decimal_places=2,null=True,max_digits=20)


	def save(self): 
		self.scope_meassurements=self.scope_meassurement_set.all()
		meassurements_list =self.scope_meassurements.values_list('total_meassurement', flat=True)
		suma=0
		for i in meassurements_list:
			suma = suma + i
		self.scope_quantity=suma	
		self.scope_price= self.scope_unt_price*self.scope_quantity
		super(Entry,self).save()




	def __str__(self):
		return self.entry_name
	class Meta:        
		verbose_name = "Project Entry"
		verbose_name_plural = "Project Entries"

	
	

class Project_Price(models.Model):
	entry               = models.OneToOneField(Entry, on_delete=models.CASCADE ,null=True,verbose_name="Entry")
	project             = models.OneToOneField(Project, on_delete=models.CASCADE ,null=True,verbose_name="Project")
	scope_price         = models.DecimalField(blank=True,decimal_places=2,null=True,max_digits=20)
	invoice_price       = models.DecimalField(blank=True,decimal_places=2,null=True,max_digits=20)
	planification_price = models.DecimalField(blank=True,decimal_places=2,null=True,max_digits=20)
	target_price        = models.DecimalField(blank=True,decimal_places=2,null=True,max_digits=20)

	class Meta:        
		verbose_name = "Project Price"
		verbose_name_plural = "Project Prices"

	def __str__(self):
		return   self.entry.entry_name

# classes para las mediciones del presupuesto , objetivo , certificacion  y planificacion

class Scope_Meassurement(models.Model):

	entry               = models.ForeignKey(Entry, on_delete=models.CASCADE ,null=True,verbose_name="Entry")
	coments             = models.CharField("coments", max_length=200, blank=True,null=True )
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
		super(Scope_Meassurement,self).save()
		
class Invoice_Meassurement(models.Model):

	entry               = models.ForeignKey(Entry, on_delete=models.CASCADE ,null=True,verbose_name="Entry")
	coments             = models.CharField("coments", max_length=200, blank=True,null=True )
	ud_type             = models.CharField("unidades", max_length=9, blank=True,null=True )
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
		super(Invoice_Meassurement,self).save()

class Planification_Meassurement(models.Model):

	entry               = models.ForeignKey(Entry, on_delete=models.CASCADE ,null=True,verbose_name="Entry")
	coments             = models.CharField("coments", max_length=200, blank=True,null=True )
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
		super(Planification_Meassurement,self).save()

class Target_Meassurement(models.Model):

	entry               = models.ForeignKey(Entry, on_delete=models.CASCADE ,null=True,verbose_name="entry")
	coments             = models.CharField("coments", max_length=200, blank=True,null=True )
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
		super(Target_Meassurement,self).save()		

#senal para creacion automatica de sets de mediciones cuando creamos una partida 

@receiver(post_save, sender=Entry)
def create_meassurments(sender, instance, created, **kwargs):
	
	if created:
		ojb=Invoice_Meassurement(entry=instance)
		ojb1=Scope_Meassurement(entry=instance)
		ojb2=Planification_Meassurement(entry=instance)
		ojb3=Target_Meassurement(entry=instance)
		ojb4=Project_Price(entry=instance)
		ojb.save()
		ojb1.save()
		ojb2.save()
		ojb3.save()
		ojb4.save()

@receiver(post_save, sender=Scope_Meassurement)
def Meassurements_scope(sender, instance, created, **kwargs):
	obj=Entry.objects.all()
	for entity in obj:
		entity.save()   
		

		





	


	


	

	