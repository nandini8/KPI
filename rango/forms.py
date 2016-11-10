from django import forms
from rango.models import Company, Metrics

class Companyform(forms.ModelForm):

	class Meta:
		model = Company
		fields = '__all__'

class Metricsform(forms.ModelForm):

	class Meta:
		model = Metrics
		fields = '__all__'