import csv, os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'tango_with_django_project.settings')

import django
django.setup()

from rango.models import Dimension

def populate():
	with open('data/Dimension.csv', 'r') as csvfile:
		spamreader = csv.DictReader(csvfile)
		for row in spamreader:
			#print(row['Dimension'],row['Level'],row['DimName'],row['ParentId'])
			d=Dimension.objects.get_or_create(dimension=row['Dimension'], level=row['Level'],
				dim_name=row['DimName'],parent_id=row['ParentId'])[0]
			print(type(d))
			d.save()
			#Dimension.objects.get(dimension=row['Dimension'])



if __name__ == '__main__':
	print('Starting rango script...')
	populate()

