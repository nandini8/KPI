import csv, os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'tango_with_django_project.settings')

import django
django.setup()
import datetime
import random
from rango.models import Dimension, MetricData, Metrics


def populate():
	d = Dimension.objects.get(id=11)
	metric = Metrics.objects.get(id=1)
	with open('data/Students.csv', 'r') as csvfile:
		Students = csv.DictReader(csvfile)
		exam_type="Oral"
		exam_date=datetime.date(2014,2,25)
		max_score=40
		for row in Students:
			m = MetricData.objects.get_or_create(dim_1=d, attr_1=row['StudentName'], attr_2=exam_type,
				date_associated=exam_date,denominator=max_score,numerator=random.randrange(15,40),
				metric_id=metric)[0]
			m.save()


if __name__ == '__main__':
	print('Starting rango script...')
	populate()

