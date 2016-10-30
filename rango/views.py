from django.shortcuts import render
from django.http import HttpResponse
from rango.models import Category, Page

def index(request):
	category_list = Category.objects.order_by('-likes')[:5]
	page_list = Page.objects.order_by('-views')[:5]

	context_dict = {'category': category_list, 'page': page_list }

	return render(request, 'rango/index.html', context_dict)

def about(request):
	context_dict = {'your_name': "NANDINI"}
	return render(request, 'rango/about.html', context_dict)

def show_category(request, category_slug_name):
	context_dict = {}

	try:
		category = Category.objects.get(slug=category_slug_name)
		page = Page.objects.filter(category=category)
		context_dict['category']= category
		context_dict['page'] = page 
		print(context_dict['page'])

	except Category.DoesNotExist:
		context_dict['category']= None
		context_dict['page'] = None

	return render(request, 'rango/context.html', context_dict)
