from django.contrib import admin
from .models import Item,Buying_Entry,Docket,Order,Time_Sheet

class AdminItem(admin.ModelAdmin):
	list_display = ['item_name','unit','provider']
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

class AdminOrder(admin.ModelAdmin):
	list_display = [ 'code', 'date','made_by', 'project', 'provider','total_price', ]
	#form = InvoiceForm
	class Meta:
		model = Order
admin.site.register(Order, AdminOrder)

class AdminTime_Sheet(admin.ModelAdmin):
	list_display = [ 'date', 'employee', 'project', 'quantity','total_price', ]
	#form = InvoiceForm
	class Meta:
		model = Time_Sheet
admin.site.register(Time_Sheet, AdminTime_Sheet)

