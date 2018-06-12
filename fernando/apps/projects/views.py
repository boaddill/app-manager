from django.shortcuts import render
from .models import *
from .forms import  Project_Creation_Form,Chapter_Creation_Form
from django.db.models import Q
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import get_object_or_404
from apps.users.decorators import superuser,is_client
from django.contrib.auth.decorators import login_required
from apps.users.models import User, Profile_Employee
from django.shortcuts import redirect
from django.template.loader import render_to_string
from django.http import JsonResponse

@superuser
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


@superuser
def project_detail(request,**kwargs):
	template = 'projects/project_detail.html'
	obj = get_object_or_404(Project, id=kwargs['id'])
	context = {'obj':obj}
	return render( request, template, context)


def project_create(request, **kwargs):
	template= 'projects/project_create.html'

	obj = get_object_or_404(Project, id=kwargs['id'])
	if request.method == 'POST':
		form = Project_Creation_Form(request.POST, instance=obj )
		if form.is_valid():
			it=form.save(commit =False)

			project_manager     =form.cleaned_data['project_manager']
			
			site_manager        =form.cleaned_data['site_manager']
			quantity_surveyor   =form.cleaned_data['quantity_surveyor']
			foreman             =form.cleaned_data['foreman']
			client              = form.cleaned_data['client']
			it.save()
			fo =it.foreman.all()
			sm = it.site_manager.all()
			qs = it.quantity_surveyor.all()
			pm = it.project_manager.all()
			if site_manager:	
				for obj in site_manager:
					if obj in sm:
						pass
					else:
						it.site_manager.add(obj)
			elif  not site_manager:
				for obj in sm:
					it.site_manager.remove(obj)

			for obj in sm:
				if obj in site_manager:
					pass
				else:
					it.site_manager.remove(obj)
			else:
				pass
			

			if quantity_surveyor:	
				for obj in quantity_surveyor:
					if obj in qs :
						pass
					else:
						it.quantity_surveyor.add(obj)
			elif  not foreman:
				for obj in fo:
					it.foreman.remove(obj)

			for obj in qs:
				if obj in quantity_surveyor:
					pass
				else:
					it.quantity_surveyor.remove(obj)
			else:
				pass

			if foreman:	
				for obj in foreman:
					if obj in fo :
						pass
					else:
						it.foreman.add(obj)
			elif  not foreman:
				for obj in fo:
					it.foreman.remove(obj)

			for obj in fo:
				if obj in foreman:
					pass
				else:
					it.foreman.remove(obj)
			else:
				pass


			if project_manager:	
				for obj in project_manager:
					if obj in pm :
						pass
					else:
						it.project_manager.add(obj)
			elif  not project_manager:
				for obj in pm:
					it.project_manager.remove(obj)

			for obj in pm :
				if obj in project_manager:
					pass
				else:
					it.project_manager.remove(obj)
			else:
				pass	
		return redirect ('projects:project_create' ,id=kwargs['id'])
	else:
		
		form=Project_Creation_Form(instance=obj)
		context = {'form':form ,'obj':obj}

		return render(request, template, context)


@superuser
def scope_detail(request,**kwargs):

	template   = 'projects/scope.html'


	project     = get_object_or_404(Project, id=kwargs['id'])
	scope       = Scope.objects.get(project=project)
	chapters    = Chapter.objects.filter(scope=scope)
	user        = get_object_or_404(User , email=request.user.email)

	context={
				
				'project':project,
				'scope':scope,
				'chapters':chapters,
				'user':user
			
	}

	return render(request,template, context )

def save_chapter_form(request, form, template_name, id):
    data = dict()
   
    if request.method == 'POST':
        if form.is_valid():
        	scope = get_object_or_404(Scope , id=id)
        	pp=form.save(commit=False)
        	pp.scope=scope
        	pp.save()
        	chapters    = Chapter.objects.filter(scope=scope)
        	project     =scope.project
        	user        = get_object_or_404(User , email=request.user.email)

        	context={
        		'project':project,
				'scope':scope,
				'chapters':chapters,
				'user':user}
        	data['form_is_valid'] = True

        	data['html_scope'] = render_to_string('projects/scope_partial.html', context)
        else:
            data['form_is_valid'] = False
    context = {'form': form , 'id':id}
    print(id)
    data['html_form'] = render_to_string(template_name, context, request=request)
    return JsonResponse(data)

@superuser				
def chapter_create(request ,**kwargs):
	id=kwargs['id']
	scope = get_object_or_404(Scope , id=id)
	
	print (scope)
	if request.method == 'POST':
		form = Chapter_Creation_Form(request.POST)
		
	else:
		form = Chapter_Creation_Form()
	return save_chapter_form(request, form, 'projects/chapters/partial_chapter_create.html',id)

@superuser
def chapter_update(request, id):
	data=dict()
	chapter = get_object_or_404(Chapter, id=id)
	scope       = Scope.objects.get(chapter=chapter)
	user        = get_object_or_404(User , email=request.user.email)
	project     = scope.project
	chapters    = Chapter.objects.filter(scope=scope)
	context={
        		'project':project,
				'scope':scope,
				'chapters':chapters,
				'user':user
				}
	if request.method == 'POST':
		form = Chapter_Creation_Form(request.POST, instance=chapter)
		if form.is_valid():
			chapter.save()
			data['form_is_valid'] = True  # This is just to play along with the existing code
			data['html_scope'] = render_to_string('projects/scope_partial.html', context)

		else:
			data['form_is_valid'] = False
	form = Chapter_Creation_Form(instance=chapter)
	data['html_form'] = render_to_string('projects/chapters/partial_chapter_update.html', {'form':form} , request=request)
	return JsonResponse(data)

@superuser
def chapter_delete(request, id):
    
    data = dict()
   
    chapter     = get_object_or_404(Chapter ,id=id)
    scope       = Scope.objects.get(chapter=chapter)
    user        = get_object_or_404(User , email=request.user.email)
    project     = scope.project
    chapters    = Chapter.objects.filter(scope=scope)
    context={
				'chapters':chapters,
				'project':project,
				'scope':scope,
				'user':user
			
	}
    if request.method == 'POST':
        chapter.delete()
        data['form_is_valid'] = True  # This is just to play along with the existing code
        data['action']='delete'
        data['html_scope'] = render_to_string('projects/scope_partial.html', context)
    else:
        context = {'chapter':chapter}
        data['html_form'] = render_to_string('projects/chapters/partial_chapter_delete.html', context, request=request,)
    return JsonResponse(data)




