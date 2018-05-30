from django.db import models
from django.db.models.signals import post_save,post_delete
from django.dispatch import receiver
from apps.invoices.models import Buying_Entry

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
	
#presupuestos {{{ pendient  asociar precio a precio capitulos }}}
class Scope (models.Model):
	code                   = models.CharField("Code", max_length=200, blank=True,null=True )
	project                = models.OneToOneField(Project, on_delete=models.CASCADE ,verbose_name="Project")
	date                   = models.DateField("Date", max_length=200, blank=True,null=True )
	valid_until            = models.DateField('Valid untill',blank=True,null=True)
	total_price            = models.DecimalField(blank=True,null=True,decimal_places=2,max_digits=10)
	total_price_invoice    = models.DecimalField(blank=True,null=True,decimal_places=2,max_digits=10)
	total_price_planif     = models.DecimalField(blank=True,null=True,decimal_places=2,max_digits=10)
	total_price_target     = models.DecimalField(blank=True,null=True,decimal_places=2,max_digits=10)
	total_price_real       = models.DecimalField('Construction actual Price',blank=True,null=True,decimal_places=2,max_digits=10)

	def __str__(self):
		return   self.project.project_name
	
	def save(self):
		#scope 
		self.chapter_prices_obj = self.chapter_set.all()
		quanties = self.chapter_prices_obj.values_list('total_price', flat=True)
		suma=0
		if quanties :
			for quantity in quanties:
				try:
					suma=suma+quantity
				except:
					quantity=0
		self.total_price = suma
		super(Scope,self).save()

		#invoice
		self.chapter_prices_invoice = self.chapter_set.all()
		quanties_invoice = self.chapter_prices_invoice.values_list('total_price_invoice', flat=True)
		suma=0
		if quanties_invoice :
			for quantity in quanties_invoice:
				try:
					suma=suma+quantity
				except:
					quantity=0
		self.total_price_invoice = suma
		super(Scope,self).save()

		#real
		self.chapter_prices_real = self.chapter_set.all()
		quanties_real = self.chapter_prices_obj.values_list('total_price_real', flat=True)
		suma=0
		if quanties_real :
			for quantity in quanties_real:
				try:
					suma=suma+quantity
				except:
					quantity=0
		self.total_price_real = suma
		super(Scope,self).save()




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
    
    


#fases del proyecto   {{ pendiente actualizar metodo save() para todas las listas de precios}}
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
	real_price        = models.DecimalField('Actual price',blank=True,decimal_places=2,null=True,max_digits=20)


	def __str__(self):
		return self.phase_name


	def save(self):
		#scope
		self.scope_meassurement = self.scope_meassurement_set.all()
		if self.scope_meassurement !=0:
			total=0
			for obj in self.scope_meassurement:
				try:
					med=obj.total_meassurement*obj.entry.scope_unt_price
					total=total+med
				except:
					pass
			self.scope_price=total		
		else :
			self.scope_price=0
			#invoice

		self.invoice_meassurement = self.invoice_meassurement_set.all()
		if self.invoice_meassurement !=0:
			total=0
			for obj in self.invoice_meassurement:
				try:
					med=obj.total_meassurement*obj.entry.invoice_unt_price
					total=total+med
				except:
					pass
			self.invoice_price=total		
		else :
			self.invoice_price=0

			#planificacion
		self.planif_meassurement = self.planification_meassurement_set.all()
		if self.planif_meassurement !=0:
			total=0
			for obj in self.planif_meassurement:
				try:
					med=obj.total_meassurement*obj.entry.planif_unt_price
					total=total+med
				except:
					pass
			self.planif_price=total		
		else :
			self.planif_price=0

			#target
		self.target_meassurement = self.target_meassurement_set.all()
		if self.planif_meassurement !=0:
			total=0
			for obj in self.target_meassurement:
				try:
					med=obj.total_meassurement*obj.entry.target_unt_price
					total=total+med
				except:
					pass
			self.target_price=total		
		else :
			self.target_price=0

			#real
		self.real_meassurement = self.real_meassurement_set.all()
		if self.real_meassurement !=0:
			total=0
			for obj in self.real_meassurement:
				try:
					med=obj.total_meassurement*obj.entry.real_unt_price
					total=total+med
				except:
					pass
			self.real_price=total		
		else :
			self.real_price=0
		super(Phase, self).save()

	#capitulos del proyecto asocia precio a suma de partidas {{{ aun pendiente}}}
class Chapter (models.Model):
	code                 = models.IntegerField( )
	chapter_name         = models.CharField("Chapter name ", max_length=200, blank=True,null=True )
	quantity		     = models.DecimalField(blank=True,decimal_places=2,null=True,max_digits=10)
	quantity_invoice     = models.DecimalField(blank=True,decimal_places=2,null=True,max_digits=10)
	quantity_planif	     = models.DecimalField(blank=True,decimal_places=2,null=True,max_digits=10)
	quantity_target	     = models.DecimalField(blank=True,decimal_places=2,null=True,max_digits=10)
	quantity_real 	     = models.DecimalField(blank=True,decimal_places=2,null=True,max_digits=10)
	total_price          = models.DecimalField(blank=True,null=True ,decimal_places=2,max_digits=10)
	total_price_invoice  = models.DecimalField(blank=True,null=True ,decimal_places=2,max_digits=10)
	total_price_planif   = models.DecimalField(blank=True,null=True ,decimal_places=2,max_digits=10)
	total_price_target   = models.DecimalField(blank=True,null=True ,decimal_places=2,max_digits=10)
	total_price_real     = models.DecimalField('Actual chapter price',blank=True,null=True ,decimal_places=2,max_digits=10)
	scope    	         = models.ForeignKey(Scope,on_delete=models.CASCADE ,blank=True,null=True , verbose_name='Scope')

	def __str__(self):
		return "%s - %s" %(self.chapter_name ,self.scope.project.project_name)

	class Meta:        
		ordering = ['code']


		#scope
	def save(self):
		self.entry_prices_obj = self.entry_set.all()
		quanties = self.entry_prices_obj.values_list('scope_price', flat=True)
		suma=0
		if quanties :
			for quantity in quanties:
				suma=suma+quantity
		self.total_price = suma

		#invoice
		self.entry_prices_obj_invoice = self.entry_set.all()
		quanties_invoice = self.entry_prices_obj_invoice.values_list('invoice_price', flat=True)
		suma=0
		if quanties_invoice :
			for quantity in quanties_invoice:
				suma=suma+quantity
		self.total_price_invoice = suma
		#planif
		self.entry_prices_obj_planif = self.entry_set.all()
		quanties_planif = self.entry_prices_obj_planif.values_list('planif_price', flat=True)
		suma=0
		if quanties_planif :
			for quantity in quanties_planif:
				suma=suma+quantity
		self.total_price_planif = suma

		#target
		self.entry_prices_obj_target = self.entry_set.all()
		quanties_target = self.entry_prices_obj_invoice.values_list('target_price', flat=True)
		suma=0
		if quanties_target :
			for quantity in quanties_target:
				suma=suma+quantity
		self.total_price_target = suma


		#real 
		self.entry_prices_obj_real = self.entry_set.all()
		quanties = self.entry_prices_obj_real.values_list('real_price', flat=True)
		suma=0
		if quanties :
			for quantity in quanties:
				suma=suma+quantity
		self.total_price_real = suma
		super(Chapter,self).save()

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


		##precios unitarios scope/planif/invoice/target{{{pendiente arreglar precios }}}
		self.entry_item_price_target_list = self.entry_item_price_set.all()
		price_list = self.entry_item_price_target_list.values_list('price_per_entry_unit',flat=True)
		suma=0
		for item in price_list:
			suma=suma+item
		self.target_unt_price   = suma
		self.scope_unt_price    = suma
		self.planif_unt_price   = suma
		self.invoice_unt_price  = suma

		#real
		self.entry_item_price_real_list = self.entry_item_price_set.all()
		price_list_real = self.entry_item_price_real_list.values_list('price_per_entry_unit_real',flat=True)
		print(price_list_real)
		suma1=0
		for item in price_list_real:
			suma1=suma1+item
		self.real_unt_price = suma1
		
		
		


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
	item                              = models.ForeignKey('invoices.Item', on_delete=models.CASCADE ,null=True,verbose_name="Item")
	quantity_per_entry_unit_scope     = models.DecimalField('quantity per entry scope',blank=True,decimal_places=2,null=True,max_digits=20)
	quantity_per_entry_unit_real      = models.DecimalField('quanatity per entry real',blank=True,decimal_places=2,null=True,max_digits=20)
	item_price                        = models.DecimalField(blank=True,decimal_places=2,null=True,max_digits=20)
	price_per_entry_unit              = models.DecimalField(blank=True,decimal_places=2,null=True,max_digits=20)
	price_per_entry_unit_real         = models.DecimalField('Actual Price per Entry unit',blank=True,decimal_places=2,null=True,max_digits=20)
	quantity_needed 		          = models.DecimalField('Estimated quantity needed',blank=True,decimal_places=2,null=True,max_digits=20)
	quantity_bought   		          = models.DecimalField('quantity_bought',blank=True,decimal_places=2,null=True,max_digits=20)
	entry                             = models.ForeignKey(Entry, on_delete=models.CASCADE ,null=True,verbose_name="Entry")
	chapter 		                  = models.ForeignKey(Chapter, on_delete=models.CASCADE ,null=True,verbose_name="Chapter")
	project 			              = models.ForeignKey(Project, on_delete=models.CASCADE ,null=True,verbose_name="Project")

	

	def save(self):
		#real ,calculo de materiales comprados /entre produccion



		self.buyings= self.buying_entry_set.all()
		lista= self.buyings.values_list('quantity',flat=True)
		try:
			suma=0
			for obj in lista:
				suma=suma+obj
			self.quantity_per_entry_unit_real=suma/self.entry.real_quantity
			self.price_per_entry_unit_real= self.item_price*self.quantity_per_entry_unit_real
			self.quantity_bought = suma
		except:
			self.quantity_per_entry_unit_real=0
			self.price_per_entry_unit_real=0
			self.quantity_bought=0



		#scope
		self.price_per_entry_unit = self.item_price*self.quantity_per_entry_unit_scope
		self.quantity_needed = self.quantity_per_entry_unit_scope*self.entry.scope_quantity
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
	phase               = models.ForeignKey(Phase,on_delete=models.CASCADE  , verbose_name='phase')

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


#recalculo de precios scope
@receiver(post_save, sender=Entry_Item_Price)
def price_save(sender, instance, created, **kwargs):

	instance.entry.save()
	
	# obj=Entry.objects.all()
	# for entity in obj:
	# 	entity.save()
	obj1=Phase.objects.all()
	for entity in obj1:
		entity.save()	  

@receiver(post_delete, sender=Entry_Item_Price)
def price_delete(sender, instance,  **kwargs):
	
	obj=Entry.objects.all()
	for entity in obj:
		entity.save()
	obj1=Phase.objects.all()
	for entity in obj1:
		entity.save() 

#meassurments
@receiver(post_save, sender=Scope_Meassurement)
def Meassurements_scope_save(sender, instance, created, **kwargs):
	instance.entry.save()
	instance.phase.save()
	# obj=Entry.objects.all()
	# for entity in obj:
	# 	entity.save()  
	# obj1=Phase.objects.all()
	# for entity in obj1:
	# 	entity.save() 
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
		
@receiver(post_save, sender=Invoice_Meassurement)
def Meassurements_invoice_save(sender, instance, created, **kwargs):
	instance.entry.save()
	instance.phase.save()
	
	# obj=Entry.objects.all()
	# for entity in obj:
	# 	entity.save()  
	# obj1=Phase.objects.all()
	# for entity in obj1:
	# 	entity.save() 
	obj2=Entry_Item_Price.objects.all()
	for entity in obj2:
		entity.save()    

@receiver(post_delete, sender=Invoice_Meassurement)
def Meassurements_invoice_delete(sender, instance,  **kwargs):
	
	obj=Entry.objects.all()
	for entity in obj:
		entity.save() 
	obj1=Phase.objects.all()
	for entity in obj1:
		entity.save()
	obj2=Entry_Item_Price.objects.all()
	for entity in obj2:
		entity.save()      

@receiver(post_save, sender=Planification_Meassurement)
def Meassurements_planif_save(sender, instance, created, **kwargs):
	instance.entry.save()
	instance.phase.save()
	
	# obj=Entry.objects.all()
	# for entity in obj:
	# 	entity.save()  
	# obj1=Phase.objects.all()
	# for entity in obj1:
	# 	entity.save() 
	obj2=Entry_Item_Price.objects.all()
	for entity in obj2:
		entity.save()    

@receiver(post_delete, sender=Planification_Meassurement)
def Meassurements_planif_delete(sender, instance,  **kwargs):
	
	obj=Entry.objects.all()
	for entity in obj:
		entity.save() 
	obj1=Phase.objects.all()
	for entity in obj1:
		entity.save()
	obj2=Entry_Item_Price.objects.all()
	for entity in obj2:
		entity.save()      		


@receiver(post_save, sender=Target_Meassurement)
def Meassurements_target_save(sender, instance, created, **kwargs):

	instance.entry.save()
	instance.phase.save()
	
	# obj=Entry.objects.all()
	# for entity in obj:
	# 	entity.save()  
	# obj1=Phase.objects.all()
	# for entity in obj1:
	# 	entity.save() 
	obj2=Entry_Item_Price.objects.all()
	for entity in obj2:
		entity.save()    

@receiver(post_delete, sender=Target_Meassurement)
def Meassurements_target_delete(sender, instance,  **kwargs):
	
	obj=Entry.objects.all()
	for entity in obj:
		entity.save() 
	obj1=Phase.objects.all()
	for entity in obj1:
		entity.save()
	obj2=Entry_Item_Price.objects.all()
	for entity in obj2:
		entity.save()      

@receiver(post_save, sender=Real_Meassurement)
def Meassurements_Real_save(sender, instance, created, **kwargs):

	instance.entry.save()
	instance.phase.save()
	
	# obj=Entry.objects.all()
	# for entity in obj:
	# 	entity.save()  
	# obj1=Phase.objects.all()
	# for entity in obj1:
	# 	entity.save() 
	obj2=Entry_Item_Price.objects.all()
	for entity in obj2:
		entity.save()    

@receiver(post_delete, sender=Real_Meassurement)
def Meassurements_Real_delete(sender, instance,  **kwargs):
	
	obj=Entry.objects.all()
	for entity in obj:
		entity.save() 
	obj1=Phase.objects.all()
	for entity in obj1:
		entity.save()
	obj2=Entry_Item_Price.objects.all()
	for entity in obj2:
		entity.save()  

#recalculo de precios despues de comprar algo
@receiver(post_save, sender=Buying_Entry)
def Meassurements_item_price_save(sender, instance, created, **kwargs):

	instance.item.save()
	
	# obj=Entry_Item_Price.objects.all()
	# for entity in obj:
	# 	entity.save()  
	
@receiver(post_delete, sender=Buying_Entry)
def Meassurements_item_price_delete(sender, instance,  **kwargs):
	
	obj=Entry_Item_Price.objects.all()
	for entity in obj:
		entity.save()  
	

#recalculo de capitulos

@receiver(post_save, sender=Entry)
def chapter_save(sender, instance, created, **kwargs):

	instance.chapter.save()
	
	# obj=Chapter.objects.all()
	# for entity in obj:
	# 	entity.save()  
	
@receiver(post_delete, sender=Entry)
def chapter_delete(sender, instance, **kwargs):
	
	obj=Chapter.objects.all()
	for entity in obj:
		entity.save()  
		
#recalculo presupuestp

@receiver(post_save, sender=Chapter)
def scope_save(sender, instance, created, **kwargs):
	instance.scope.save()
	
	
	
	# obj=Scope.objects.all()
	# for entity in obj:
	# 	entity.save()  
	
@receiver(post_delete, sender=Chapter)
def scope_delete(sender, instance,  **kwargs):
	
	objs=Scope.objects.all()
	for entity in objs:
		entity.save()  
		


	

	