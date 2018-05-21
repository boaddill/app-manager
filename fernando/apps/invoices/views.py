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



def item_filter_list(request):
	data = dict()
	items = Item.objects.all()
	query = request.GET.get('q', "")
	if query:
		items =items.filter(item_name__icontains=query)
	data['html'] = render_to_string('items/partial_item_list.html', 
            {'items': items}, request=request)
	return JsonResponse(data)





