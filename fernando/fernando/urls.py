
from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.contrib .auth import urls as auth_urls
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views



urlpatterns = [
    path('admin/', admin.site.urls,name='admin'),
    path('', include('apps.users.urls')),
    path('', include('apps.profiles.urls')),
    path('', include('apps.invoices.urls')),
    path('', include('apps.projects.urls')),
    path('accounts/', include('django.contrib.auth.urls'))
    

]



if settings.DEBUG :
	urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
   
	urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

