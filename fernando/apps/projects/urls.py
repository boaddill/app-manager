import re 
from django.urls import path
from  .views import  (project_list,project_detail,
					 project_create,
					 scope_detail,chapter_create,chapter_delete,chapter_update

)

app_name = 'projects'
urlpatterns = [
   
    path('project_list', project_list, name='project_list'),
    path('project_detail/<id>/', project_detail, name='project_detail'),
    path('project_create/<id>/', project_create, name='project_create'),
    path('scope_detail/<id>', scope_detail, name='scope_detail'),
    path('chapter_create/<id>', chapter_create, name='chapter_create'),
    path('chapter_delete/<id>', chapter_delete, name='chapter_delete'),
    path('chapter_update/<id>', chapter_update, name='chapter_update'),
    
]