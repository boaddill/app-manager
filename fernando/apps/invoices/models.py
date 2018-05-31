from django.db.models.signals import  post_delete, post_save
from django.dispatch import receiver
from django.db import models
import datetime
from .signals.signals import my_signal



class Item(models.Model):
	code             = models.CharField("Code", max_length=200, blank=True,null=True )
	item_name        = models.CharField("Item name", max_length=200, blank=True,null=True )
	unit             = models.CharField("Units", max_length=200, blank=True,null=True )
	item_description = models.TextField("Item description", max_length=200, blank=True,null=True )
	provider		 = models.ForeignKey('users.Profile_Provider',on_delete=models.CASCADE ,blank=True,null=True,verbose_name='Provider')
	def __str__(self):
		return self.item_name


class Order(models.Model):
	code             = models.CharField("Code", max_length=200, blank=True,null=True )
	date             = models.DateField('date',auto_now=False,blank=True,null=True)
	made_by          = models.ForeignKey('users.Profile_Employee', on_delete=models.CASCADE , blank=True,null=True,verbose_name='Made by' )
	provider         = models.ForeignKey('users.Profile_Provider' ,on_delete=models.CASCADE ,blank=True,null=True, verbose_name='Provider')
	project          = models.ForeignKey('projects.Project',on_delete=models.CASCADE , blank=True,null=True,verbose_name='Project' )
	total_price      = models.DecimalField(blank=True,null=True,decimal_places=2,max_digits=10)


	def __str__(self):
		return self.code
	
	def save(self):
		self.entries = self.buying_entry_set.all()
		price_list=self.entries.values_list('total_price', flat=True)

		self.entries2 = self.time_sheet_set.all()
		price_list2=self.entries2.values_list('total_price', flat=True)
		suma_entries=0
		suma_timesheets=0
		for i in price_list:
			suma_entries += i
		for i in price_list2:
			suma_timesheets += i

		self.total_price=suma_entries+suma_timesheets
		super(Order,self).save()

class Docket(models.Model):
	code             = models.CharField("Code", max_length=200, blank=True,null=True )
	date             = models.DateField('date',auto_now=False)
	client           = models.ForeignKey('users.Profile_Client' ,on_delete=models.CASCADE ,blank=True,null=True, verbose_name='Client')
	project          = models.ForeignKey('projects.Project',on_delete=models.CASCADE , blank=True,null=True,verbose_name='Project' )
	total_price      = models.DecimalField(blank=True,null=True,decimal_places=2,max_digits=10)

	def __str__(self):
		return self.code
	
	def save(self):
		self.entries = self.buying_entry_set.all()
		price_list=self.entries.values_list('total_price', flat=True)

		self.entries2 = self.time_sheet_set.all()
		price_list2=self.entries2.values_list('total_price', flat=True)
		suma_entries=0
		suma_timesheets=0
		for i in price_list:
			suma_entries += i
		for i in price_list2:
			suma_timesheets += i

		self.total_price=suma_entries+suma_timesheets
		super(Docket,self).save()

class Invoice(models.Model):
	invoice_number  = models.CharField("Invoice number", max_length=200, blank=True,null=True )
	invoice_date    = models.DateField('invoice date',blank=True,null=True)
	client          = models.ForeignKey('users.Profile_Client' ,on_delete=models.CASCADE ,blank=True,null=True, verbose_name='Client')
	project         = models.ForeignKey('projects.Project',on_delete=models.CASCADE , blank=True,null=True,verbose_name='Project' )
	total_price     = models.DecimalField(blank=True,null=True,decimal_places=2,max_digits=10)
	gst             = models.DecimalField(blank=True,null=True,decimal_places=2,max_digits=10)
	price_due_to	= models.DecimalField(blank=True,null=True,decimal_places=2,max_digits=10)


	def __str__(self):
		return  '%s %s' %(self.invoice_number, self.client)

class Buying_Entry(models.Model):

	date             = models.DateField('date',auto_now=False)
	item             = models.ForeignKey('projects.Entry_Item_Price' , on_delete=models.CASCADE, blank=True,null=True,verbose_name='Item' )
	units            = models.CharField("units", max_length=200, blank=True,null=True ,default='unidades')
	quantity		 = models.DecimalField(blank=True,null=True, decimal_places=2,max_digits=10)
	price            = models.DecimalField(blank=True,null=True ,decimal_places=2,max_digits=10)
	total_price      = models.DecimalField(blank=True,null=True ,decimal_places=2,max_digits=10)
	provider         = models.ForeignKey('users.Profile_Provider', on_delete=models.CASCADE , blank=True,null=True,verbose_name='Provider' )
	invoiced         = models.BooleanField(default=False,)
	order            = models.ForeignKey(Order,default=None ,on_delete=models.CASCADE , blank=True,null=True,verbose_name='Order' )
	docket           = models.ForeignKey(Docket,default=None ,on_delete=models.CASCADE , blank=True,null=True,verbose_name='Docket')
	invoice          = models.ForeignKey(Invoice,default=None ,on_delete=models.CASCADE ,blank=True,null=True, verbose_name='Invoice' )


	class Meta:        
		verbose_name = "Entry"
		verbose_name_plural = "Entries"


	def save(self):
		self.price = self.item.item_price
		self.total_price=self.quantity*self.price
		super(Buying_Entry,self).save()


	def __str__(self):
		pass

		return '%s %s %s'  %(self.date, self.item, self.total_price)

class Time_Sheet(models.Model):

	date             = models.DateField('date',auto_now=False)
	employee         = models.ForeignKey('users.Profile_Employee', on_delete=models.CASCADE , blank=True,null=True,verbose_name='Employee' )
	units            = models.CharField("units", max_length=200, blank=True,null=True,default='hours' )
	quantity		 = models.DecimalField(blank=True,null=True,decimal_places=2,max_digits=5)
	coments          = models.TextField("coments", max_length=400, blank=True,null=True,default='coments' )
	total_price      = models.DecimalField(blank=True,null=True,decimal_places=2,max_digits=10)
	project          = models.ForeignKey('projects.Project',on_delete=models.CASCADE , blank=True,null=True,verbose_name='Project' )
	invoiced         = models.BooleanField(default=False,)
	order            = models.ForeignKey(Order,default=None ,on_delete=models.CASCADE , blank=True,null=True,verbose_name='Order' )
	docket           = models.ForeignKey(Docket,default=None ,on_delete=models.CASCADE , blank=True,null=True,verbose_name='Docket')
	invoice          = models.ForeignKey(Invoice,default=None ,on_delete=models.CASCADE ,blank=True,null=True, verbose_name='Invoice' )

	class Meta:        
		verbose_name = "Time sheet"
		verbose_name_plural = "Time Sheets"

	def save(self):
		my_signal.send(sender=Time_Sheet,instance=self)
		self.total_price=self.quantity*self.employee.hour_price
		super(Time_Sheet,self).save()

	

	
@receiver(post_save, sender=Buying_Entry)
def save_Docket(sender,created, instance,**kwargs):
	obj=instance.docket
	obj1=instance.order
	if obj:
		obj.save()
	else:
		query =Docket.objects.all()
		for obj in query:
			obj.save()
	if obj1:
		obj1.save()
	else:
		query =Order.objects.all()
		for obj in query:
			obj.save()



@receiver(post_delete, sender=Buying_Entry)
def delete_Docket(sender, instance,**kwargs):
	print("hola")
	obj=instance.docket
	obj2=instance.order
	obj.save()
	obj2.save()

	
@receiver(post_save, sender=Time_Sheet)
def timesheet_save_Docket(sender,created, instance,**kwargs):
	obj=instance.docket
	obj1=instance.order
	obj.save()
	obj1.save()


@receiver(post_delete, sender=Time_Sheet)
def timesheet_delete_Docket(sender, instance,**kwargs):
	print("hola")
	obj=instance.docket
	obj2=instance.order
	obj.save()
	obj2.save()

	






















  


 


