from django.conf.urls import url
from django.contrib import admin
from rango import views

urlpatterns = [
	url(r'^$', views.index, name='index'),
	url(r'^about/$', views.about, name='about'),
	url(r'^category/(?P<category_slug_name>[\w\-]+)/$', views.show_category, name='show_category')
]