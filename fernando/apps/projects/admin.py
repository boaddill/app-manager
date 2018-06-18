from django.contrib import admin
from .models import (Project,Scope, Entry,Scope_Meassurement,
					Invoice_Meassurement,Planification_Meassurement,
					Phase,Target_Meassurement,Chapter, Entry_Item_Price,
					Real_Meassurement
					)


class AdminProject(admin.ModelAdmin):
	list_display = ['project_number','project_name','client','state']
	class Meta:
		model =  Project
admin.site.register(Project, AdminProject)


class AdminScope(admin.ModelAdmin):
	list_display = ['id','code','project','date','total_price','total_price_invoice','total_price_target','total_price_real','valid_until']
	#form = InvoiceForm
	class Meta:
		model =  Scope
admin.site.register(Scope, AdminScope)




class AdminChapter(admin.ModelAdmin):
	list_display = [  'code','chapter_name','total_price','total_price_real','scope']
	#form = InvoiceForm
	class Meta:
		model =  Chapter
admin.site.register(Chapter, AdminChapter)

class AdminEntry(admin.ModelAdmin):
	list_display = ['id','code','units','entry_name','scope_unt_price','target_unt_price','real_unt_price',
					'scope_quantity','real_quantity','scope_price','real_price' ,
					 'chapter','risk_factor'

					 ]
	#form = InvoiceForm
	class Meta:
		model =  Entry
admin.site.register(Entry, AdminEntry)

class AdminPhase(admin.ModelAdmin):
	list_display = ['id','phase_code','phase_name','coments','start_date','end_date','scope_price',
			'invoice_price','planif_price','target_price','real_price']
	#form = InvoiceForm
	class Meta:
		model =  Phase
admin.site.register(Phase, AdminPhase)




class AdminScope_Meassurement(admin.ModelAdmin):
	list_display = ['entry','ud_type','coments','quantity','width','high','wide','total_meassurement' ,'phase']
	#form = InvoiceForm
	class Meta:
		model =  Scope_Meassurement
admin.site.register(Scope_Meassurement, AdminScope_Meassurement)



class AdminScope_Invoice_Meassurement(admin.ModelAdmin):
	list_display = ['entry','ud_type','quantity','width','high','wide','total_meassurement']
	#form = InvoiceForm
	class Meta:
		model =  Invoice_Meassurement
admin.site.register(Invoice_Meassurement, AdminScope_Invoice_Meassurement)


class AdminScope_Planification_Meassurement(admin.ModelAdmin):
	list_display = ['entry','ud_type','quantity','width','high','wide','total_meassurement']
	#form = InvoiceForm
	class Meta:
		model =  Planification_Meassurement
admin.site.register(Planification_Meassurement, AdminScope_Planification_Meassurement)

class AdminScope_Target_Meassurement(admin.ModelAdmin):
	list_display = ['entry','ud_type','quantity','width','high','wide','total_meassurement']
	#form = InvoiceForm
	class Meta:
		model =  Target_Meassurement
admin.site.register(Target_Meassurement, AdminScope_Target_Meassurement)


class AdminScope_Real_Meassurement(admin.ModelAdmin):
	list_display = ['entry','ud_type','quantity','width','high','wide','total_meassurement']
	#form = InvoiceForm
	class Meta:
		model =  Real_Meassurement
admin.site.register(Real_Meassurement, AdminScope_Real_Meassurement)


class AdminEntry_Item_Price(admin.ModelAdmin):
	list_display = ['item','quantity_per_entry_unit_scope',   'quantity_per_entry_unit_real','price_per_entry_unit_scope','item_price','price_per_entry_unit_real','quantity_needed','entry']
	#form = InvoiceForm
	class Meta:
		model =  Entry_Item_Price
admin.site.register(Entry_Item_Price, AdminEntry_Item_Price)


	


















