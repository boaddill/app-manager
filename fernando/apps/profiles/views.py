from django.shortcuts import render
from django.shortcuts import render,get_object_or_404
from django.http import HttpResponseRedirect
from django.contrib import auth
from django.shortcuts import redirect
from apps.users.decorators import superuser,is_client
from django.db import transaction
from apps.users.models import Profile_Client, User,Profile_Employee,Profile_Provider
from django.contrib import messages
from django.urls import reverse
from django.db.models import Q
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.core.exceptions import ObjectDoesNotExist



@superuser
def client_list(request):
    action='cuenta:client_list'
    
    client_profile = Profile_Client.objects.all()
    
    query = request.GET.get('q', "")
    if query:
        client_profile=client_profile.filter(
            Q(company_name__icontains=query)|
            Q(company_director__icontains=query)|
            Q(company_email__icontains=query )).distinct()
    paginator = Paginator(client_profile, 8)
    page = request.GET.get('page', 1)
    try:
        users = paginator.page(page)
    except PageNotAnInteger:
        users = paginator.page(1)
    except EmptyPage:
        users = paginator.page(paginator.num_pages)
    return render(request, 'profiles/client_profile_list.html', {'clients': users,
    'action':action } )



@is_client
@superuser
def profiles_detail(request ,*args, **kwargs):

    if kwargs['action']=='Profile_Client':
        A=Profile_Client
        B='profiles:client_list'
        template='profiles/client_detail.html'
    if kwargs['action']=='Profile_Employee':
        A=Profile_Employee
        B='profiles:employee_list'
        template='profiles/emplyee_detail.html'
    if kwargs['action']=='Profile_Provider':
        A=Profile_Provider
        B='profiles:provider_list'
        template='profiles/provider_detail.html'
    try:
        entity=A.objects.get(id=kwargs['id'])
    except :
        entity=None
    
    if entity:
        return render(request, template , {'entity': entity})
    else:
        return redirect(B)

    
      

    


