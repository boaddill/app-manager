import re 
from django.urls import path
from  .views import  client_list,profiles_detail



app_name = 'profiles'
urlpatterns = [
   
    
    path('client_list', client_list, name='client_list'),
    path('profiles_detail/<action>/<id>', profiles_detail, name='profiles_detail'),




    ]