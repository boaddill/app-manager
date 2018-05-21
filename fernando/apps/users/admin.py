from django.contrib import admin
from .models import User, Profile_Client,Profile_Employee,Profile_Provider

class AdminUser(admin.ModelAdmin):
	list_display = ['email']
	#form = InvoiceForm
	class Meta:
		model =  User
admin.site.register(User, AdminUser)



class AdminProfile_Client(admin.ModelAdmin):
	list_display = ['user', 'company_name','company_director']
	#form = InvoiceForm
	class Meta:
		model =  Profile_Client


admin.site.register(Profile_Client, AdminProfile_Client)




class  AdminProfile_Employee(admin.ModelAdmin):
	list_display = ['user','employee_name','position' ]
	#form = InvoiceForm
	class Meta:
		model =  Profile_Employee


admin.site.register(Profile_Employee, AdminProfile_Employee )

class AdminProfile_Provider(admin.ModelAdmin):
	list_display = ['user', 'company_name','company_director' ]
	#form = InvoiceForm
	class Meta:
		model =  Profile_Provider


admin.site.register(Profile_Provider, AdminProfile_Provider)




