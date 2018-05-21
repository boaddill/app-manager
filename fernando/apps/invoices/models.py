from django.db import models
import datetime


class Tasks (models.Model):
	task_name      = models.CharField("Task name ", max_length=200, blank=True,null=True )
	Project  	   = models.ForeignKey('projects.Project',on_delete=models.CASCADE , verbose_name='Project' )
	
class Item(models.Model):
	item_name        = models.CharField("Item name", max_length=200, blank=True,null=True )
	unit             = models.CharField("Units", max_length=200, blank=True,null=True )
	item_price       = models.FloatField('Item price',default=None)
	item_description = models.TextField("Item description", max_length=200, blank=True,null=True )
	provider		 = models.ForeignKey('users.Profile_Provider',on_delete=models.CASCADE ,blank=True,null=True,verbose_name='Provider')


class Order(models.Model):
	pass



class Docket(models.Model):
	pass


class Invoice(models.Model):
	
	invoice_number  = models.CharField("Invoice number", max_length=200, blank=True,null=True )
	invoice_date    = models.DateField('invoice date',blank=True,null=True)
	client          = models.ForeignKey('users.Profile_Client' ,on_delete=models.CASCADE ,blank=True,null=True, verbose_name='Client')


	def __str__(self):
		return  '%s %s' %(self.invoice_number, self.client)



class Buying_Entry(models.Model):

	item             = models.ForeignKey(Item , on_delete=models.CASCADE, verbose_name='Item' )
	production_date  = models.DateField('date',auto_now=False)
	units            = models.CharField("units", max_length=200, blank=True,null=True )
	quantity		 = models.IntegerField()
	project          = models.ForeignKey('projects.Project',on_delete=models.CASCADE , verbose_name='Project' )
	task             = models.ForeignKey(Tasks, on_delete=models.CASCADE , verbose_name='TASKS' )
	invoiced         = models.BooleanField(default=False,)
	total_price      = models.FloatField()
	invoice          = models.ForeignKey(Invoice,default=None ,on_delete=models.CASCADE , verbose_name='Invoice' )
	order            = models.ForeignKey(Order,default=None ,on_delete=models.CASCADE , verbose_name='Order' )
	docket           = models.ForeignKey(Docket,default=None ,on_delete=models.CASCADE , verbose_name='Docket' )























  


 


