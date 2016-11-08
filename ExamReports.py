import os, django, datetime, collections
from django.db.models import Sum, Count
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'tango_with_django_project.settings' )
django.setup()

from rango.models import MetricData, Dimension

def AllStudentsAllExams():
	AllSubjectsAllExams_list = list()
	d=dict()
	print('{:>4} {:<15} {:<10} {:<10} {:<10} {:>10} {:>10} {:>15}'.format("Num","Student","Sem","Subject",
		"Exam_type","Marks","Max","Percentage"))
	id = 0
	metric_obj = MetricData.objects.all()
	for m in metric_obj:
		parent_obj = m.dim_1.parent
		subject =  ''.join(x[0] for x in m.dim_1.dim_name.split())				#creating abbreviations for subjects
		id = id + 1
		#print('{:>4} {:<15} {:<10} {:<10} {:<10} {:>10} {:>10} {:15.2f}'.format(m.id, m.attr_1, parent_obj.dim_name, subject, m.attr_2, m.numerator
		#	,m.denominator,(m.numerator * 100) / m.denominator))
		d = {'attr_1' : m.attr_1, 'parent' : parent_obj.dim_name, 'subject' : subject, 'attr_2': m.attr_2, 'numerator' :m.numerator,
		'denominator': m.denominator, 'percentage':float((m.numerator * 100) / m.denominator)}	
		AllSubjectsAllExams_list.append(d)


def AllStudentsAllSubjects():
	AllStudentsAllSubjects_list = list()
	#print('{:>4} {:<15} {:<10} {:<10} {:>10} {:>10} {:>15}'.format("Num","Student","Sem","Subject","Marks","Max","Percentage"))
	m_list = MetricData.objects.raw('Select id, dim_1_id, Sum(numerator) as numerator, attr_1, sum(denominator) as denominator from rango_metricdata group by attr_1, dim_1_id ')
	id = 0
	for m in m_list:
		id += 1
		dim = Dimension.objects.get(id=m.dim_1_id)
		dim1 = Dimension.objects.get(id = dim.parent.id)
		subject =  ''.join(x[0] for x in dim.dim_name.split())
		print('{:>4} {:<15} {:<10} {:<10} {:>10} {:>10} {:13.2f}'.format(id,m.attr_1, dim1.dim_name, subject,m.numerator,m.denominator, m.numerator * 100 / m.denominator))
		d = {'attr_1' : m.attr_1,'sem' : dim1.dim_name, 'subject' : subject, 'numerator' :m.numerator,
		'denominator': m.denominator, 'percentage':float((m.numerator * 100) / m.denominator)}
		AllStudentsAllSubjects_list.append(d)
	return(AllStudentsAllSubjects_list)


def AllStudentsAllSems():
	print("Num \t","Student \t","Sem \t","Marks \t","Max \t","Percentage")




def AllStudents():
	print('{:>4} {:<15} {:>10} {:>10} {:>15}'.format("Num","Student","Marks","Max","Percentage"))
	m_list = MetricData.objects.raw('SELECT id, attr_1, Sum(numerator) as numerator, Sum(denominator) as denominator,Sum(numerator) * 100 / Sum(denominator) as percentage from rango_metricdata GROUP BY attr_1')
	for m in m_list:
		print('{:>4} {:<15} {:>10} {:>10} {:13.2f}%'.format(m.id,m.attr_1,m.numerator,m.denominator,m.percentage))
		

def AllSubjectsAllExams():
	print('{:>4} {:<15} {:>10} {:>10} {:>15} {:>15} {:>15}'.format("Num","Sem","Subject","Exam_type","Marks","Max","Percentage"))
	m_list = MetricData.objects.raw('select id, dim_1_id, attr_2, sum(numerator) as numerator, sum(denominator) as denominator, numerator * 100 / denominator as percentage  from rango_metricdata group by dim_1_id, attr_2')
	id=0
	for m in m_list:
		id += 1
		dim = Dimension.objects.get(id=m.dim_1_id)
		dim1 = Dimension.objects.get(id = dim.parent.id)
		subject =  ''.join(x[0] for x in dim.dim_name.split())

		print('{:>4} {:<15} {:>10} {:>10} {:>15} {:>15} {:13.2f}'.format(id,dim1.dim_name,subject,m.attr_2,m.numerator,m.denominator,m.percentage))


def AllSubjects():
	print('{:>4} {:<15} {:>10} {:>10} {:>15} {:>15}'.format("Num","Sem","Subject","Marks","Max","Percentage"))
	m_list = MetricData.objects.raw('select id, dim_1_id, sum(numerator) as numerator, sum(denominator) as denominator, numerator * 100 / denominator as percentage  from rango_metricdata group by dim_1_id')
	id=0
	for m in m_list:
		id += 1
		dim = Dimension.objects.get(id=m.dim_1_id)
		dim1 = Dimension.objects.get(id = dim.parent.id)
		subject =  ''.join(x[0] for x in dim.dim_name.split())
		print('{:>4} {:<15} {:>10} {:>10} {:>15} {:13.2f}'.format(id,dim1.dim_name,subject,m.numerator,m.denominator,m.percentage))



def AllSems():
	print('{:>4} {:<15} {:>10} {:>15} {:>15}'.format("Num","Sem","Marks","Max","Percentage"))

	sem_list = Dimension.objects.raw('select id from rango_dimension where id in (select parent_id from rango_dimension where id in (select dim_1_id from rango_metricdata group by dim_1_id))')
	for sem in sem_list:
		m_list = MetricData.objects.raw('select  id, sum(numerator) as numerator , sum(denominator) as denominator,sum(numerator) * 100 / sum(denominator) as percentage from rango_metricdata where dim_1_id in (select id from rango_dimension where parent_id =' + str(sem.id) + ')')
		id = 0
		for m in m_list:
			id += 1
			print('{:>4} {:<15} {:>10} {:>15} {:13.2f}'.format(id, sem.dim_name, m.numerator, m.denominator , m.percentage))



def AllSubjectsForStudent(student_name):
	#print("Student name: ", student_name)
	#print('{:>4} {:<15} {:<10} {:<10} {:>10} {:>10} {:>10}'.format("Num","Sem","Subject","Oral","Practical","Written","Total"))

	oral_list = MetricData.objects.raw('select id, dim_1_id, numerator , denominator from rango_metricdata where attr_1 = "'+student_name+'" and attr_2 = "Oral" group by dim_1_id')
	written_list = MetricData.objects.raw('select id, dim_1_id, numerator, denominator from rango_metricdata where attr_1 = "'+student_name+'" and attr_2 = "Written" group by dim_1_id')
	practical_list = MetricData.objects.raw('select id, dim_1_id, numerator, denominator from rango_metricdata where attr_1 = "'+student_name+'" and attr_2 = "Practical" group by dim_1_id')

	id = 0
	list_dict =[]
	for o, w, p in zip(oral_list, written_list, practical_list):
		id += 1
		dim = Dimension.objects.get(id=o.dim_1_id)
		dim1 = Dimension.objects.get(id = dim.parent.id)
		subject =  ''.join(x[0] for x in dim.dim_name.split())
		perc_oral = o.numerator * 100 / o.denominator
		perc_prac = p.numerator * 100 / p.denominator
		perc_written = w.numerator * 100 / w.denominator
		total = (o.numerator + p.numerator + w.numerator) * 100 / (o.denominator+p.denominator+w.denominator)

		list_dict.append({'id': id, 'sem': dim1.dim_name, 'subject': subject, 'Oral': perc_oral, 'Written': perc_written, 'Practical': perc_prac, 'total': total})
		#print('{:>4} {:<15} {:<10} {:<10} {:9.2f}% {:9.2f}% {:9.2f}%'.format(id, dim1.dim_name, subject , perc_oral , perc_prac, perc_written, total))
	return(list_dict) 




if __name__ == '__main__':
	#AllStudentsAllExams()
	AllStudentsAllSubjects()
	#AllStudents()
	#AllSubjectsAllExams()
	#AllSubjects()
	#AllSems()

	#AllSubjectsForStudent(input('Enter name of the student: '))

	#student_name = input('Enter name of the student: ')
	#l =	AllSubjectsForStudent(student_name)

