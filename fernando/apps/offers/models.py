from django.db import models
from django.db.models.signals import post_save,post_delete,m2m_changed
from django.dispatch import receiver



class Price_Solicitude(models.Model):
	code             = models.CharField("Code", max_length=200, blank=True,null=True )
	date             = models.DateField('date',auto_now=False,blank=True,null=True)
	made_by          = models.ForeignKey('users.Profile_Employee', on_delete=models.CASCADE , blank=True,null=True,verbose_name='Made by' )
	items   	     = models.ManyToManyField('invoices.Item',blank=True,verbose_name="Items")
	provider         = models.ForeignKey('users.Profile_Provider' ,on_delete=models.CASCADE ,blank=True,null=True, verbose_name='Provider')
	project          = models.ForeignKey('projects.Project',on_delete=models.CASCADE , blank=True,null=True,verbose_name='Project' )
	

	def __str__(self):
		return "%s - %s" %(self.provider ,self.project.project_name)


class Solicitude_Entry(models.Model):

	item              = models.OneToOneField('projects.Entry_Item_Price' , on_delete=models.CASCADE, verbose_name='Item' )
	units             = models.CharField("units", max_length=200, blank=True,null=True ,default='units')
	quantity		  = models.DecimalField(blank=True,null=True, decimal_places=2,max_digits=10)
	price_solicitude  = models.ForeignKey(Price_Solicitude , on_delete=models.CASCADE, verbose_name='price_solicitude' )
	
	def save(self):
		self.quantity = self.item.quantity_needed
		super(Solicitude_Entry, self).save()

	class Meta:        
		verbose_name = "Solicitude of prices"
		verbose_name_plural = "Solicitude of prices"