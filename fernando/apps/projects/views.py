from django.shortcuts import render
from .models import *
from django.db.models import Q
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import get_object_or_404

def project_list(request, **kwargs):
	user    = Project.objects.all().order_by('-date')
	template = 'projects/project_list.html'
	query = request.GET.get('q', "")
	if query:
		user=user.filter(
        	Q(project_name__icontains=query)|
        	Q(client__icontains=query)|
        	q(project_manager__icontains=query)
            )
	paginator = Paginator(user, 10)
	page = request.GET.get('page', 1)
	try:
		users = paginator.page(page)
	except PageNotAnInteger:
		users = paginator.page(1)
	except EmptyPage:
		users = paginator.page(paginator.num_pages)
	return render(request, template, {'projects': users})

def project_detail(request,**kwargs):
	template = 'projects/project_detai.html'
	obj = get_object_or_404(Poject, id=kwargs['id'])
	return ( request, template, {'obj':obj})


def project_create(request, **kwargs):
	pass


def project_update(request, **kwargs):
	pass


def project_delete(request, **kwargs):
	pass