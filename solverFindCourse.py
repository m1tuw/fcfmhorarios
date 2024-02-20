from important_stuff import *
from ramos import *
from itertools import product
from solver import *

# Schedule, string, string, Database -> list<Course>
def solverFindCourse(sch, earliest, latest, db):
	good_courses = []
	for course in db.database:
		# agregar el filtro por especialidad aqui cdo no m de paja
		if filter(course, earliest, latest) == 1:
			if sch.check_clash(course) == 0:
				good_courses.append(course)
	return good_courses