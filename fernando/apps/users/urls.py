import re 
from django.urls import path
from django.contrib.auth import views as auth_views
from  .views import  (
	home , user_list, user_create,user_update,user_delete,user_filter_list,
	validate_username

		)
from django.contrib.auth import views as auth_views


app_name = 'users'
urlpatterns = [
   
    path('', home, name='home'),
    path('user_list', user_list, name='user_list'),
    path('user_create', user_create, name='user_create'),
    path('user/<id>/update', user_update, name='user_update'),
    path('user/<id>/delete', user_delete, name='user_delete'),
    path('user_filter_list', user_filter_list, name='user_filter_list'),
    path('login/', auth_views.login,{'template_name':'users/login.html' }, name='login'),
    path('logout/', auth_views.logout,{'next_page': '/'}, name='logout'),
    path('ajax/validate_username/', validate_username, name='validate_username'),
    
]




