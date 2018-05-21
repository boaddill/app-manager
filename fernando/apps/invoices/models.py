from django.db.models.signals import post_save
from django.dispatch import receiver
from django.db import models
import datetime


class Tasks (models.Model):
	task_name      = models.CharField("Task name ", max_length=200, blank=True,null=True )
	Project  	   = models.ForeignKey('projects.Project',on_delete=models.CASCADE , verbose_name='Project' )
	
class Item(models.Model):
	code             = models.CharField("Code", max_length=200, blank=True,null=True )
	item_name        = models.CharField("Item name", max_length=200, blank=True,null=True )
	unit             = models.CharField("Units", max_length=200, blank=True,null=True )
	item_price       = models.FloatField('Item price',default=None)
	item_description = models.TextField("Item description", max_length=200, blank=True,null=True )
	provider		 = models.ForeignKey('users.Profile_Provider',on_delete=models.CASCADE ,blank=True,null=True,verbose_name='Provider')
	def __str__(self):
		return self.item_name

class Order(models.Model):
	pass



class Docket(models.Model):
	code             = models.CharField("Code", max_length=200, blank=True,null=True )
	date             = models.DateField('date',auto_now=False)
	client           = models.ForeignKey('users.Profile_Client' ,on_delete=models.CASCADE ,blank=True,null=True, verbose_name='Client')
	project          = models.ForeignKey('projects.Project',on_delete=models.CASCADE , blank=True,null=True,verbose_name='Project' )
	total_price      = models.FloatField(blank=True,null=True)

	def __str__(self):
		return self.code
	


	def save(self):
		self.entries = self.buying_entry_set.all()
		price_list=self.entries.values_list('total_price', flat=True)
		suma=0
		for i in price_list:
			suma += i
		self.total_price=suma
		super(Docket,self).save()
 



class Invoice(models.Model):
	
	invoice_number  = models.CharField("Invoice number", max_length=200, blank=True,null=True )
	invoice_date    = models.DateField('invoice date',blank=True,null=True)
	client          = models.ForeignKey('users.Profile_Client' ,on_delete=models.CASCADE ,blank=True,null=True, verbose_name='Client')


	def __str__(self):
		return  '%s %s' %(self.invoice_number, self.client)



class Buying_Entry(models.Model):

	
	date             = models.DateField('date',auto_now=False)
	item             = models.ForeignKey(Item , on_delete=models.CASCADE, verbose_name='Item' )
	units            = models.CharField("units", max_length=200, blank=True,null=True )
	quantity		 = models.IntegerField(blank=True,null=True)
	total_price      = models.FloatField(blank=True,null=True)
	project          = models.ForeignKey('projects.Project',on_delete=models.CASCADE , blank=True,null=True,verbose_name='Project' )
	task             = models.ForeignKey(Tasks, on_delete=models.CASCADE ,blank=True,null=True, verbose_name='Task' )
	provider         = models.ForeignKey('users.Profile_Provider', on_delete=models.CASCADE , blank=True,null=True,verbose_name='Provider' )
	invoiced         = models.BooleanField(default=False,)
	invoice          = models.ForeignKey(Invoice,default=None ,on_delete=models.CASCADE ,blank=True,null=True, verbose_name='Invoice' )
	order            = models.ForeignKey(Order,default=None ,on_delete=models.CASCADE , blank=True,null=True,verbose_name='Order' )
	docket           = models.ForeignKey(Docket,default=None ,on_delete=models.CASCADE , blank=True,null=True,verbose_name='Docket')

	class Meta:        
		verbose_name = "Entry"
		verbose_name_plural = "Entries"



	def save(self):
		self.total_price=self.quantity*self.item.item_price
		super(Buying_Entry,self).save()

	def __str__(self):

		return '%s %s %s'  %(self.date, self.item, self.total_price)



	

	





















  


 


