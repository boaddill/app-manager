from django.contrib import admin
from .models import Item,Buying_Entry,Docket

class AdminItem(admin.ModelAdmin):
	list_display = ['item_name','unit','item_price','provider']
	#form = InvoiceForm
	class Meta:
		model =  Item
admin.site.register(Item, AdminItem)


class AdminBuying_Entry(admin.ModelAdmin):
	list_display = [ 'date', 'item','quantity', 'total_price', 'provider']
	#form = InvoiceForm
	class Meta:
		model =  Buying_Entry
admin.site.register(Buying_Entry, AdminBuying_Entry)



class AdminDocket(admin.ModelAdmin):
	list_display = [ 'code', 'date','client', 'project', 'total_price', ]
	#form = InvoiceForm
	class Meta:
		model = Docket
admin.site.register(Docket, AdminDocket)

