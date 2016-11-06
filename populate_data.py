#populate_data.py

import os, django, csv, datetime, random
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'tango_with_django_project.settings' )
django.setup()

from rango.models import *

def populate():
	subjects_list, students_list = list(), list()
	x = list()

	#exam_types = {'type of exam': [month for even sem, month for odd sem, minimum marks, maximum marks]}
	exam_types = {'Oral': [2, 8, 15, 40], 'Written': [4, 10, 25, 60], 'Practical': [6, 12, 35, 100]}
	semester = {'Sem I': 2014, 'Sem II': 2014, 'Sem III': 2015, 'Sem IV': 2015, 'Sem V': 2016, 'Sem VI': 2016}

	with open('data/Students.csv') as Students_csv:
		students_dict = csv.DictReader(Students_csv)
		students_list = list(students_dict)


	metric_obj = Metrics.objects.get(id=1)


	semesters = Dimension.objects.filter(parent_id=2)
	sem_index = 0

	for sem in semesters:
		print(sem.dim_name)
		exam_year = semester[sem.dim_name]
		print(exam_year)
		subjects = Dimension.objects.filter(parent_id=sem.id)
		sem_index += 1
		exam_day = 0

		for subject in subjects:
			print("\t", subject.dim_name)
			exam_day += 1

			for exam_type in exam_types.keys():
				exam_month = exam_types[exam_type][sem_index % 2]
				#print(exam_month)
				exam_date = datetime.date(exam_year, exam_month, exam_day)
				print("\t\t", exam_type, exam_date)
				min1 = exam_types[exam_type][2]
				max1 = exam_types[exam_type][3]

				for student in students_list:
					#print("\t\t\t", student['StudentName'])
					num = random.randrange(min1, max1)
					print(subject, student['StudentName'], exam_type, exam_date, metric_obj, num, max1 )
					break

					'''m = MetricData.objects.get_or_create(dim_1=subject, attr_1=student['StudentName'],
						attr_2= exam_type,
						date_associated=exam_date, metric_id=metric_obj,
						numerator=num, denominator=max1 )[0]
					m.save()'''
					print(student['StudentName']," created")

if __name__ == '__main__':
	print("Starting to populate data")
	populate()











	


