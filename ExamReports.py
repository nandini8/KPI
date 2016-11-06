import os, django, datetime
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'tango_with_django_project.settings' )
django.setup()

from rango.models import MetricData, Dimension

def AllStudentsAllExams():
	print("Num \t","Student \t","Sem \t\t","Subject \t","Exam_type \t","Marks \t","Max \t","Percentage")
	m = MetricData.objects.get(id=1)
	parent=m.dim_1.parent_id
	sem = Dimension.objects.get(id=parent)
	print(m.id,"\t",m.attr_1,"\t",sem.dim_name,"\t",m.dim_1.dim_name,"\t",m.attr_2,"\t",m.numerator,"\t",m.denominator,"\t",
		(m.numerator * 100) / m.denominator)


def AllStudentsAllSubjects():
	print("Num \t","Student \t","Sem \t","Subject \t","Marks \t","Max \t","Percentage")




def AllStudentsAllSems():
	print("Num \t","Student \t","Sem \t","Marks \t","Max \t","Percentage")



def AllStudents():
	print("Num \t","Student \t","Marks \t","Max \t","Percentage")


def AllSubjectsAllExams():
	print("Num \t","Sem \t","Subject \t","Exam_type \t","Marks \t","Max \t","Percentage")



def AllSubjects():
	print("Num \t","Sem \t","Subject \t","Marks \t","Max \t","Percentage")


def AllSems():
	print("Num \t","Sem \t","Marks \t","Max \t","Percentage")


if __name__ == '__main__':
	AllStudentsAllExams()