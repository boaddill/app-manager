from django.shortcuts import render
from .models import  User
from django.http import JsonResponse
from django.template.loader import render_to_string
from .forms import UserCreationForm
from django.shortcuts import render,get_object_or_404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .decorators import superuser,is_client
from django.contrib.auth.decorators import login_required


def home(request):
    context = {}
    return render(request, "users/home.html" , context)

    

@superuser
def user_list(request):
    action=""
    user = User.objects.all()
    query = request.GET.get('q', "")
    if query:
        user=user.filter(
            email__icontains=query)
    paginator = Paginator(user, 10)
    page = request.GET.get('page', 1)
    try:
        users = paginator.page(page)
    except PageNotAnInteger:
        users = paginator.page(1)
    except EmptyPage:
        users = paginator.page(paginator.num_pages)
    return render(request, 'users/client_list.html', {'users': users, 'action':action})



@superuser
def save_user_form(request, form, template_name, action,id):
    data = dict()
    if request.method == 'POST':
        if form.is_valid():
            user_type=form.cleaned_data['user_type']
            email=form.cleaned_data['email']

            form.save()
            if user_type=='1':
                user=User.objects.get(email=email)
                user.is_client=True
                user.is_visitor=False
                user.is_employee=False
                user.is_provider=False
                user.save()
            if user_type=='2':
                user=User.objects.get(email=email)
                user.is_employee=True
                user.is_visitor=False
                user.is_provider=False
                user.is_client=False
                user.save()
            if user_type=='3':
                user=User.objects.get(email=email)
                user.is_provider=True
                user.is_visitor=False
                user.is_client=False
                user.is_employee=False
                user.save()
            if user_type=='4':
                user=User.objects.get(email=email)
                user.is_superuser=True
                user.is_visitor=False
                user.is_client=False
                user.is_employee=False
                user.is_provider=True
                user.save()
            data['form_is_valid'] = True
            if action == 'create':
                users = User.objects.all().order_by('id').reverse()[:1]
                data['action']='create'
                data['html_user_list'] = render_to_string('users/partial_user_list.html', {
                    'users': users})

            if action == 'update':
                user = User.objects.filter(email=email)
                data['action']='update'
                data['html_user_list'] = render_to_string('users/partial_user_list.html', {'users': user})
        else:
            data['form_is_valid'] = False
    context = {'form': form}
    data['html_form'] = render_to_string(template_name, context, request=request)
    return JsonResponse(data)

@superuser				
def user_create(request):
	
	if request.method == 'POST':
		form = UserCreationForm(request.POST)
		
	else:
		form = UserCreationForm()
	
	return save_user_form(request, form, 'users/partial_user_create.html','create',id)



@superuser
def user_update(request, id):
    user = get_object_or_404(User, id=id)
    if request.method == 'POST':
        form = UserCreationForm(request.POST, instance=user)
    else:
        form = UserCreationForm(instance=user)
    return save_user_form(request, form, 'users/partial_user_update.html','update' ,id)



@superuser
def user_delete(request, id):
    user = get_object_or_404(User, id=id)
    data = dict()
    if request.method == 'POST':
        user.delete()
        data['form_is_valid'] = True  # This is just to play along with the existing code
        users1 = User.objects.all()
        data['action']='delete'
        data['html_user_list'] = render_to_string('users/partial_user_list.html', {
            'users': users1
        })
    else:
        context = {'user': user}
        data['html_form'] = render_to_string('users/partial_user_delete.html',

            context,
            request=request,
        )
    return JsonResponse(data)

@superuser
def user_filter_list(request):

    data = dict()
    users = User.objects.all()
    query = request.GET.get('q', "")
    if query:
        users =users.filter(email__icontains=query)

    data['html'] = render_to_string('users/partial_user_list.html', 
            {'users': users}, request=request)
    return JsonResponse(data)


def validate_username(request,*args,**kwargs):
    email = request.GET.get('email', None)
    data = {
        'is_taken': User.objects.filter(email__iexact=email).exists()
    }
    return JsonResponse(data)


    
    




