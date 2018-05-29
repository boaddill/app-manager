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
	
	project_name         = models.CharField(max_length=200, blank=True, null=True)
	project_number       = models.CharField(max_length=200, blank=True)
	date                 = models.DateField(blank=True, null=True)
	project_address      = models.CharField(max_length=200, blank=True,null=True)
	start_date           = models.DateField(blank=True, null=True)
	end_date             = models.DateField(blank=True, null=True)
	project_manager      = models.ManyToManyField('users.Profile_Employee', blank=True,verbose_name="Project manager",related_name='project_manager')
	site_manager         = models.ManyToManyField('users.Profile_Employee', blank=True ,verbose_name="site manager",related_name='site_manager')
	quantity_surveyor    = models.ManyToManyField('users.Profile_Employee', blank=True ,verbose_name="quantyty surveyor",related_name='quantity_surveyor')
	foreman              = models.ManyToManyField('users.Profile_Employee', blank=True ,verbose_name="Foreman",related_name='foreman')
	client               = models.ForeignKey('users.Profile_client',on_delete=models.CASCADE,null=True ,blank=True,verbose_name="client",related_name="client")
	state                = models.CharField(max_length=3, choices = STATE_TYPES,default=WAITING)
	
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
	scope_price		  = models.DecimalField(blank=True,decimal_places=2,null=True,max_digits=20)
	invoice_price     = models.DecimalField(blank=True,decimal_places=2,null=True,max_digits=20)
	planif_price      = models.DecimalField(blank=True,decimal_places=2,null=True,max_digits=20)
	target_price      = models.DecimalField(blank=True,decimal_places=2,null=True,max_digits=20)
	real_price        = models.DecimalField(blank=True,decimal_places=2,null=True,max_digits=20)


	def __str__(self):
		return self.phase_name


	def save(self):

		self.scope_meassurement = self.scope_meassurement_set.all().distinct()
		if self.scope_meassurement:
			total=0
			for obj in self.scope_meassurement:
				med=obj.total_meassurement*obj.entry.scope_unt_price
				total=total+med
			self.scope_price=total
		super(Phase, self).save()



	#capitulos del proyecto
class Chapter (models.Model):
	code              = models.IntegerField( )
	chapter_name      = models.CharField("Chapter name ", max_length=200, blank=True,null=True )
	quantity		  = models.DecimalField(blank=True,decimal_places=2,null=True,max_digits=10)
	total_price       = models.DecimalField(blank=True,null=True ,decimal_places=2,max_digits=10)
	scope    	      = models.ForeignKey(Scope,on_delete=models.CASCADE ,blank=True,null=True , verbose_name='Scope')

	def __str__(self):
		return "%s - %s" %(self.chapter_name ,self.scope.project.project_name)

	class Meta:        
		ordering = ['code']
	

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
	chapter    	          = models.ForeignKey(Chapter,on_delete=models.CASCADE ,blank=True ,null=True, verbose_name='Chapter - Project')
	project    	          = models.ForeignKey(Project,on_delete=models.CASCADE ,blank=True ,null=True, verbose_name='Project')
	scope_quantity		  = models.DecimalField(blank=True,decimal_places=2,null=True,max_digits=20)
	invoice_quantity	  = models.DecimalField(blank=True,decimal_places=2,null=True,max_digits=20)
	planif_quantity	      = models.DecimalField(blank=True,decimal_places=2,null=True,max_digits=20)
	target_quantity	      = models.DecimalField(blank=True,decimal_places=2,null=True,max_digits=20)
	real_quantity	      = models.DecimalField(blank=True,decimal_places=2,null=True,max_digits=20)
	scope_unt_price	      = models.DecimalField(blank=True,decimal_places=2,null=True,max_digits=20)
	invoice_unt_price     = models.DecimalField(blank=True,decimal_places=2,null=True,max_digits=20)
	planif_unt_price      = models.DecimalField(blank=True,decimal_places=2,null=True,max_digits=20)
	target_unt_price      = models.DecimalField(blank=True,decimal_places=2,null=True,max_digits=20)
	real_unt_price        = models.DecimalField(blank=True,decimal_places=2,null=True,max_digits=20)
	scope_price		      = models.DecimalField(blank=True,decimal_places=2,null=True,max_digits=20)
	invoice_price         = models.DecimalField(blank=True,decimal_places=2,null=True,max_digits=20)
	planif_price          = models.DecimalField(blank=True,decimal_places=2,null=True,max_digits=20)
	target_price          = models.DecimalField(blank=True,decimal_places=2,null=True,max_digits=20)
	real_price            = models.DecimalField(blank=True,decimal_places=2,null=True,max_digits=20)

	
	def save(self): 


		##precios unitarios
		self.entry_item_price_target_list = self.entry_item_price_set.all()
		price_list = self.entry_item_price_target_list.values_list('price_per_entry_unit',flat=True)
		suma=0
		for item in price_list:
			suma=suma+item
		self.target_unt_price = suma
		self.scope_unt_price  = suma
		


		#medidas
		#scope
		self.scope_meassurements=self.scope_meassurement_set.all()
		scope_list =self.scope_meassurements.values_list('total_meassurement', flat=True)
		suma=0
		for i in scope_list:
			suma = suma + i
		self.scope_quantity=suma
		if self.scope_quantity!=0 and self.scope_unt_price!=None  	:
			self.scope_price= self.scope_unt_price*suma
		else:
			self.scope_price=0		
		

		#invoice
		self.invoice_meassurements=self.invoice_meassurement_set.all()
		invoices_list =self.invoice_meassurements.values_list('total_meassurement', flat=True)
		suma=0
		for i in invoices_list:
			suma = suma + i
		self.invoice_quantity=suma
		if self.invoice_quantity!=0 and self.invoice_unt_price!=None:
			self.invoice_price= self.invoice_unt_price*self.invoice_quantity
		else:
			self.invoice_price=0

		#planif
		self.planif_meassurements=self.planification_meassurement_set.all()
		planif_list =self.planif_meassurements.values_list('total_meassurement', flat=True)
		suma=0
		for i in planif_list:
			suma = suma + i
		self.planif_quantity=suma
		if self.planif_quantity!=0 and self.planif_unt_price!=None:
			self.planif_price= self.planif_unt_price*self.planif_quantity
		else:
			self.planif_price=0

		#target
		self.target_meassurements=self.target_meassurement_set.all()
		target_list =self.target_meassurements.values_list('total_meassurement', flat=True)
		suma=0
		for i in target_list:
			suma = suma + i
		self.target_quantity=suma
		if self.target_quantity!=0 and self.target_unt_price!=None:
			self.target_price= self.target_unt_price*self.target_quantity
		else:
			self.target_price=0

		#real
		self.real_meassurements=self.real_meassurement_set.all()
		real_list =self.real_meassurements.values_list('total_meassurement', flat=True)
		suma=0
		for i in real_list:
			suma = suma + i
		self.real_quantity=suma
		if self.real_quantity!=0 and self.real_unt_price!=None:
			self.real_price= self.real_unt_price*self.real_quantity
		else:
			self.real_price=0

						

		super(Entry,self).save()
#fin metodo save para Entries 


	def __str__(self):
		return "%s - %s" %(self.entry_name ,self.project)
	class Meta:        
		verbose_name = "Project Entry"
		verbose_name_plural = "Project Entries"

	
class Entry_Item_Price(models.Model):
	item                     = models.ForeignKey('invoices.Item', on_delete=models.CASCADE ,null=True,verbose_name="Item")
	quantity_per_entry_unit  = models.DecimalField(blank=True,decimal_places=2,null=True,max_digits=20)
	item_price               = models.DecimalField(blank=True,decimal_places=2,null=True,max_digits=20)
	price_per_entry_unit     = models.DecimalField(blank=True,decimal_places=2,null=True,max_digits=20)
	quantity_needed 		 = models.DecimalField(blank=True,decimal_places=2,null=True,max_digits=20)
	entry                    = models.ForeignKey(Entry, on_delete=models.CASCADE ,null=True,verbose_name="Entry")
	chapter 		         = models.ForeignKey(Chapter, on_delete=models.CASCADE ,null=True,verbose_name="Chapter")
	project 			     = models.ForeignKey(Project, on_delete=models.CASCADE ,null=True,verbose_name="Project")

	

	def save(self):
		self.price_per_entry_unit = self.item_price*self.quantity_per_entry_unit
		self.quantity_needed = self.quantity_per_entry_unit*self.entry.scope_quantity
		super(Entry_Item_Price,self).save()

	class Meta:        
		verbose_name = "Project Price"
		verbose_name_plural = "Project Prices"

	def __str__(self):
		return "%s - %s" %(self.item ,self.project)

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

class Real_Meassurement(models.Model):

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
		verbose_name = "Real Meassurement"
		verbose_name_plural = "Real Meassurements"

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
		super(Real_Meassurement,self).save()		

#senal para creacion automatica de sets de mediciones cuando creamos una partida 


@receiver(post_save, sender=Entry)
def create_meassurments(sender, instance, created, **kwargs):
	
	if created:
		ojb=Invoice_Meassurement(entry=instance)
		ojb1=Scope_Meassurement(entry=instance)
		ojb2=Planification_Meassurement(entry=instance)
		ojb3=Target_Meassurement(entry=instance)
		ojb5=Real_Meassurement(entry=instance)
		ojb4=Entry_Item_Price_Target(entry=instance)
		ojb.save()
		ojb1.save()
		ojb2.save()
		ojb3.save()
		ojb4.save()
		ojb5.save()


#recaluclo de precios
@receiver(post_save, sender=Entry_Item_Price)
def price_save(sender, instance, created, **kwargs):
	
	obj=Entry.objects.all()
	for entity in obj:
		entity.save()  

@receiver(post_delete, sender=Entry_Item_Price)
def price_delete(sender, instance,  **kwargs):
	
	obj=Entry.objects.all()
	for entity in obj:
		entity.save() 
	   

@receiver(post_save, sender=Scope_Meassurement)
def Meassurements_scope_save(sender, instance, created, **kwargs):
	
	obj=Entry.objects.all()
	for entity in obj:
		entity.save()  
	obj1=Phase.objects.all()
	for entity in obj1:
		entity.save() 
	obj2=Entry_Item_Price.objects.all()
	for entity in obj2:
		entity.save()    

@receiver(post_delete, sender=Scope_Meassurement)
def Meassurements_scope_delete(sender, instance,  **kwargs):
	
	obj=Entry.objects.all()
	for entity in obj:
		entity.save() 
	obj1=Phase.objects.all()
	for entity in obj1:
		entity.save()
	obj2=Entry_Item_Price.objects.all()
	for entity in obj2:
		entity.save()      
		
#hacer lo mismo con resto de mediciones  importante
		





	


	


	

	