from django.db import models
from django.template.defaultfilters import slugify
from django.utils import timezone
#updating for KPI project
#Thank you for you comment
# Create your models here.

class Category(models.Model):
	name = models.CharField(max_length=50, unique=True)
	views = models.IntegerField(default=0)
	likes = models.IntegerField(default=0)
	slug = models.SlugField(blank=True, unique=True)

	class Meta():
		verbose_name_plural = 'Categories'

	def save(self, *args, **kwargs):
		self.slug = slugify(self.name)
		super(Category, self).save(*args, **kwargs)

	def __str__(self):
		return self.name 

class Page(models.Model):
	category = models.ForeignKey(Category)
	title = models.CharField(max_length=50)
	url = models.URLField()
	views = models.IntegerField(default=0)

	def __str__(self):
		return self.title

class Metrics(models.Model):
	metric_name = models.CharField(max_length=50)
	metric_type = models.CharField(max_length=10)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)
	row_status = models.IntegerField(blank=False)

	def __str__(self):
		return self.metric_name

class Dimension(models.Model):
	dimension = models.CharField(max_length=50)
	level = models.IntegerField(blank=False)
	dim_name = models.CharField(max_length=50)
	parent_id = models.IntegerField(blank=False)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)

	def __str__(self):
		return self.dimension
	

class MetricData(models.Model):
	dim_1 = models.ForeignKey(Dimension)
	#dim_2 = models.ForeignKey(Dimension)
	#dim_3 = models.ForeignKey(Dimension)
	attr_1 = models.CharField(max_length=50)
	attr_2 = models.CharField(max_length=50)
	attr_3 = models.CharField(max_length=50)
	date_associated = models.DateField()
	metric_id = models.ForeignKey(Metrics)
	numerator = models.IntegerField()
	denominator = models.IntegerField()
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)
	row_status = models.IntegerField(blank=False, default=True)
	loaded_by = models.CharField(max_length=50)




