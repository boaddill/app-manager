import re 
from django.urls import path
from  .views import  project_list,project_detail



app_name = 'projects'
urlpatterns = [
   
    path('project_list', project_list, name='project_list'),
    path('project_detail', project_detail, name='project_detail'),

    ]