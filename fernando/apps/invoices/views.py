from django.shortcuts import render
from apps.users.models import  User
from django.http import JsonResponse
from django.template.loader import render_to_string
from django.shortcuts import render,get_object_or_404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from apps.users.decorators import superuser,is_client
from django.contrib.auth.decorators import login_required
from .models import Item


def item_view(request):
	item=Item.objects.all()
	query = request.GET.get('q', "")
	if query:
		item=item.filter(
			item_name__icontains=query)

	paginator = Paginator(item, 10)
	page = request.GET.get('page', 1)
	try:
		items = paginator.page(page)
	except PageNotAnInteger:
		items = paginator.page(1)
	except EmptyPage:
		items = paginator.page(paginator.num_pages)
	return render(request, 'items/item_list.html', {'items': items})


@superuser
def save_item_form(request, form, template_name, action,id):
    data = dict()
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            
            data['form_is_valid'] = True
            if action == 'create':
                items = Items.objects.all().order_by('id').reverse()[:1]
                data['action']='create'
                data['html_item_list'] = render_to_string('items/partial_item_list.html', {
                    'items': items})

            if action == 'update':
                item = Item.objects.filter(id=id)
                data['action']='update'
                data['html_item_list'] = render_to_string('item/partial_item_list.html', {'items': item})
        else:
            data['form_is_valid'] = False
    context = {'form': form}
    data['html_form'] = render_to_string(template_name, context, request=request)
    return JsonResponse(data)

@superuser				
def item_create(request):
	
	if request.method == 'POST':
		form = ItemCreationForm(request.POST)
		
	else:
		form = ItemCreationForm()
	
	return save_user_form(request, form, 'items/partial_item_form.html','create',id)


@superuser
def item_update(request, id):
    item = get_object_or_404(Item, id=id)
    if request.method == 'POST':
        form = ItemCreationForm(request.POST, instance=item)
    else:
        form = ItemCreationForm(instance=item)
    return save_item_form(request, form, 'users/partial_item_update.html','update' ,id)


@superuser
def item_delete(request, id):
    item = get_object_or_404(Item, id=id)
    data = dict()
    if request.method == 'POST':
        item.delete()
        data['form_is_valid'] = True  # This is just to play along with the existing code
        items1 = User.objects.all()
        data['action']='delete'
        data['html_item_list'] = render_to_string('items/partial_item_list.html', {
            'items': items1
        })
    else:
        context = {'item': item}
        data['html_form'] = render_to_string('item/partial_item_delete.html',

            context,
            request=request,
        )
    return JsonResponse(data)




def item_filter_list(request):
	data = dict()
	items = Item.objects.all()
	query = request.GET.get('q', "")
	if query:
		items =items.filter(item_name__icontains=query)
	data['html'] = render_to_string('items/partial_item_list.html', 
            {'items': items}, request=request)
	return JsonResponse(data)





