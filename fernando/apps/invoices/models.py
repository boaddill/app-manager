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


class Order(models.Model):
	pass



class Docket(models.Model):
	code             = models.CharField("Code", max_length=200, blank=True,null=True )
	date             = models.DateField('date',auto_now=False)
	client           = models.ForeignKey('users.Profile_Client' ,on_delete=models.CASCADE ,blank=True,null=True, verbose_name='Client')



	

	


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
	quantity		 = models.IntegerField()
	total_price      = models.FloatField()
	project          = models.ForeignKey('projects.Project',on_delete=models.CASCADE , verbose_name='Project' )
	task             = models.ForeignKey(Tasks, on_delete=models.CASCADE , verbose_name='Task' )
	provider         = models.ForeignKey('users.Profile_Provider', on_delete=models.CASCADE , verbose_name='Provider' )
	invoiced         = models.BooleanField(default=False,)
	invoice          = models.ForeignKey(Invoice,default=None ,on_delete=models.CASCADE , verbose_name='Invoice',related_name='invoice' )
	order            = models.ForeignKey(Order,default=None ,on_delete=models.CASCADE , verbose_name='Order' ,related_name='order')
	docket           = models.ForeignKey(Docket,default=None ,on_delete=models.CASCADE , verbose_name='Docket',related_name='docket' )























  


 


