import os, django, datetime
from django.db.models import Sum, Count
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'tango_with_django_project.settings' )
django.setup()

from rango.models import MetricData, Dimension

def AllStudentsAllExams():

	print('{:>4} {:<15} {:<10} {:<10} {:<10} {:>10} {:>10} {:>15}'.format("Num","Student","Sem","Subject",
		"Exam_type","Marks","Max","Percentage"))

	metric_obj = MetricData.objects.all()
	for m in metric_obj:
		parent_obj = m.dim_1.parent
		subject =  ''.join(x[0] for x in m.dim_1.dim_name.split())				#creating abbreviations for subjects

		print('{:>4} {:<15} {:<10} {:<10} {:<10} {:>10} {:>10} {:15.2f}'.format(m.id, m.attr_1, parent_obj.dim_name, subject, m.attr_2, m.numerator
			,m.denominator,(m.numerator * 100) / m.denominator))


def AllStudentsAllSubjects():
	
	print('{:>4} {:<15} {:<10} {:<10} {:>10} {:>10} {:>15}'.format("Num","Student","Sem","Subject","Marks","Max","Percentage"))


	metric_obj = MetricData.objects.values('attr_1').extra(select={'id', }).annotate(numerator=Sum('numerator'))
	print(metric_obj)

	#m_obj = MetricData.objects.values('attr_1','attr_2').annotate(denominator=Sum('denominator'))
	#print(m_obj)

	
	for m in metric_obj:
		print(m['attr_1'])
		subject =  ''.join(x[0] for x in m.dim_1.dim_name.split())				#creating abbreviations for subjects
	



		#print('{:>4} {:<15} {:<10} {:<10} {:<10} {:>10} {:>10} {:15.2f}'.format(m.id, m.attr_1, parent_obj.dim_name, subject, m.attr_2, m.numerator
		#	,m.denominator,(m.numerator * 100) / m.denominator))




def AllStudentsAllSems():
	print("Num \t","Student \t","Sem \t","Marks \t","Max \t","Percentage")



def AllStudents():
	print('{:>4} {:<15} {:>10} {:>10} {:>15}'.format("Num","Student","Marks","Max","Percentage"))
	m_list = MetricData.objects.raw('SELECT id, attr_1, Sum(numerator) as numerator, Sum(denominator) as denominator,Sum(numerator) * 100 / Sum(denominator) as percentage from rango_metricdata GROUP BY attr_1')
	for m in m_list:
		print('{:>4} {:<15} {:>10} {:>10} {:>15}'.format(m.id,m.attr_1,m.numerator,m.denominator,m.p))
		




def AllSubjectsAllExams():
	print("Num \t","Sem \t","Subject \t","Exam_type \t","Marks \t","Max \t","Percentage")



def AllSubjects():
	print("Num \t","Sem \t","Subject \t","Marks \t","Max \t","Percentage")


def AllSems():
	print("Num \t","Sem \t","Marks \t","Max \t","Percentage")


if __name__ == '__main__':
	#AllStudentsAllExams()
	#AllStudentsAllSubjects()
	AllStudents()