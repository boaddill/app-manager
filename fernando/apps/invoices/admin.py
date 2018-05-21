from django.contrib import admin
from .models import Item

class AdminItem(admin.ModelAdmin):
	list_display = ['item_name','unit','item_price','provider']
	#form = InvoiceForm
	class Meta:
		model =  Item
admin.site.register(Item, AdminItem)
