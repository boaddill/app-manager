from django.contrib import admin
from .models import (Project,Scope, Entry,Scope_Meassurement,
					Invoice_Meassurement,Planification_Meassurement,
					Phase,Target_Meassurement,Chapter, Project_Price
					)


class AdminProject(admin.ModelAdmin):
	list_display = ['project_number','project_name','client','project_manager','state']
	class Meta:
		model =  Project
admin.site.register(Project, AdminProject)

class AdminScope(admin.ModelAdmin):
	list_display = ['id','code','project','date','total_price','valid_until']
	#form = InvoiceForm
	class Meta:
		model =  Scope
admin.site.register(Scope, AdminScope)


class AdminChapter(admin.ModelAdmin):
	list_display = [ 'id', 'code','chapter_name','total_price','scope']
	#form = InvoiceForm
	class Meta:
		model =  Chapter
admin.site.register(Chapter, AdminChapter)

class AdminEntry(admin.ModelAdmin):
	list_display = ['code','entry_name','description','scope_unt_price','scope_quantity','scope_price' , 'chapter']
	#form = InvoiceForm
	class Meta:
		model =  Entry
admin.site.register(Entry, AdminEntry)

class AdminPhase(admin.ModelAdmin):
	list_display = ['phase_code','phase_name','coments','start_date','end_date']
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
admin.site.register(Target_Meassurement, AdminScope_Planification_Meassurement)

class AdminScopeProject_Price(admin.ModelAdmin):
	list_display = ['entry','project','scope_price','invoice_price','planification_price','target_price']
	#form = InvoiceForm
	class Meta:
		model =  Project_Price
admin.site.register(Project_Price, AdminScopeProject_Price)



	


















