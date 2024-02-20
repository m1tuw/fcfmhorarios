from important_stuff import *
from ramos import *
from itertools import product

# retorna 1 si se queda y 0 si se va al agua:p
def filter(course, earliest, latest):
	for recitation in course.recitations:
		start = recitation[1]
		end = recitation[2]
		if timeToMinutes(start) < timeToMinutes(earliest):
			return 0
		if timeToMinutes(end) > timeToMinutes(latest):
			return 0
	for lecture in course.lectures:
		start = lecture[1]
		end = lecture[2]
		if timeToMinutes(start) < timeToMinutes(earliest):
			return 0
		if timeToMinutes(end) > timeToMinutes(latest):
			return 0
	return 1

def solve(dict_of_courses, earliest, latest):
	all_courses = [] # lista de listas de cursos. cada lista contiene los cursos con cierto id
	good_schedules = []

	for value in dict_of_courses.values():
		# value es una lista de cursos
		courselist = []
		for course in value:
			if filter(course, earliest, latest) == 1:
				courselist.append(course)

		all_courses.append(courselist) # value: lista de cursos

	for comb in product(*all_courses):
		curr_schedule = Schedule()
		for course in comb:
			curr_schedule.add_course(course)
		if curr_schedule.count_clashes() == 0:
			good_schedules.append(curr_schedule)

	return good_schedules