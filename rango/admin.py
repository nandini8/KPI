from django.contrib import admin
from rango.models import Category, Page, Dimension, MetricData, Metrics

# Register your models here.

class PageAdmin(admin.ModelAdmin):
	list_display = ('title', 'views', 'url', 'category')

class CategoryAdmin(admin.ModelAdmin):
	prepopulated_fields = {'slug': ('name', )}
	list_display = ('name', 'views')


admin.site.register(Category, CategoryAdmin)
admin.site.register(Page, PageAdmin)
admin.site.register(Dimension)
admin.site.register(MetricData)
admin.site.register(Metrics)
