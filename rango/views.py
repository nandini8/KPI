from django.shortcuts import render, render_to_response
from django.http import HttpResponse
from rango.models import Category, Page, MetricData, Metrics, Dimension
from graphos.sources.model import ModelDataSource
from graphos.renderers import gchart
import ExamReports
import json




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

def category(request):
	category_list = Category.objects.order_by('likes')
	context_dict = {"category": category_list, }
	return render(request, "rango/category.html", context_dict)

def page(request):
		page_list = Page.objects.order_by('views')
		context_dict = {'pages': page_list, }
		return render(request, 'rango/pages.html', context_dict)

def AllStudentsAllSubjectschart(request):

	list_dict = ExamReports.AllStudentsAllSubjects()
	#print(list_dict)
	#context_dict = {'list' : list_dict}
	#return render(request, 'rango/chart.html', context_dict)

	js_data = json.dumps(list_dict)
	#print("sdcsc")
	#print(js_data)
	return render_to_response('rango/AllStudentsAllSubjects.html', {'list': js_data})

def chart(request):
	
	list_dict = ExamReports.AllSubjectsForStudent('Angel')

	#context_dict = {'list' : list_dict}
	#return render(request, 'rango/chart.html', context_dict)

	js_data = json.dumps(list_dict)
	return render_to_response('rango/chart.html', {'list': js_data})




