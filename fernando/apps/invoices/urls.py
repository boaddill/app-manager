import re 
from django.urls import path
from .views import item_view ,item_filter_list




app_name = 'invoices'
urlpatterns = [
   
    
    path('item', item_view, name='item_view'),
    path('item_filter_list', item_filter_list, name='item_filter_list'),
    


    ]