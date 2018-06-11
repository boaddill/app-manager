from django.contrib import admin
from .models import Price_Solicitude , Solicitude_Entry

class AdminPrice_Solicitude(admin.ModelAdmin):
	list_display = ['code','date','made_by','provider','project']
	#form = InvoiceForm
	class Meta:
		model =  Price_Solicitude
admin.site.register(Price_Solicitude,AdminPrice_Solicitude )

class AdminSolicitude_Entry(admin.ModelAdmin):
	list_display = ['item','units','quantity','price_solicitude']
	#form = InvoiceForm
	class Meta:
		model =  Solicitude_Entry
admin.site.register(Solicitude_Entry,AdminSolicitude_Entry )


	
	