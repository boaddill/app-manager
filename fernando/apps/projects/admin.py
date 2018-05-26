from django.contrib import admin
from .models import (Project,Scope, Task,Scope_Meassurement,
					Invoice_Meassurement,Planification_Meassurement,
					Phase,Target_Meassurement,
					)


class AdminProject(admin.ModelAdmin):
	list_display = ['project_number','project_name','client','project_manager','state']
	class Meta:
		model =  Project
admin.site.register(Project, AdminProject)

class AdminScope(admin.ModelAdmin):
	list_display = ['project','date','total_price','valid_until']
	#form = InvoiceForm
	class Meta:
		model =  Scope
admin.site.register(Scope, AdminScope)

class AdminTask(admin.ModelAdmin):
	list_display = ['code','task_name','description']
	#form = InvoiceForm
	class Meta:
		model =  Task
admin.site.register(Task, AdminTask)

class AdminPhase(admin.ModelAdmin):
	list_display = ['phase_code','phase_name','coments','start_date','end_date']
	#form = InvoiceForm
	class Meta:
		model =  Phase
admin.site.register(Phase, AdminPhase)


class AdminScope_Meassurement(admin.ModelAdmin):
	list_display = ['task','ud_type','quantity','width','high','wide','total_meassurement']
	#form = InvoiceForm
	class Meta:
		model =  Scope_Meassurement
admin.site.register(Scope_Meassurement, AdminScope_Meassurement)



class AdminScope_Invoice_Meassurement(admin.ModelAdmin):
	list_display = ['task','ud_type','quantity','width','high','wide','total_meassurement']
	#form = InvoiceForm
	class Meta:
		model =  Invoice_Meassurement
admin.site.register(Invoice_Meassurement, AdminScope_Invoice_Meassurement)


class AdminScope_Planification_Meassurement(admin.ModelAdmin):
	list_display = ['task','ud_type','quantity','width','high','wide','total_meassurement']
	#form = InvoiceForm
	class Meta:
		model =  Planification_Meassurement
admin.site.register(Planification_Meassurement, AdminScope_Planification_Meassurement)

class AdminScope_Target_Meassurement(admin.ModelAdmin):
	list_display = ['task','ud_type','quantity','width','high','wide','total_meassurement']
	#form = InvoiceForm
	class Meta:
		model =  Target_Meassurement
admin.site.register(Target_Meassurement, AdminScope_Planification_Meassurement)




















