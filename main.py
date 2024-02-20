from important_stuff import *
from solver import *
from solverFindCourse import *

def main():
	db = Database()
	db.load()
	# open a text menu here or something
	print("0 - buscar un horario con los ramos que quieras^^")
	print("1 - buscar un ramo que te quede con tu horario...")
	prompt = input()
	if prompt == "0":
		findSchedule(db)
	if prompt == "1":
		findCourse(db)
	else:
		"normalmente mostraría aquí un mensaje de crasheo pero no lo implementé.... asiq ola"

def findCourse(db):
	found = []
	prompt = ""
	print("Ingresa el código del ramo que deseas incluir en tu horario con la sección (Ej: CC3101-2).")
	print("Para terminar, ingresa ok")
	while prompt != "ok":

		id = input()
		if id == "ok":
			break

		query = db.searchWithSection(id)
		if query == None:
			print("ese curso no existe :c")
		else:
			found.append(query)
			print(query)
			print("Se ha agregado el curso a tu horario.")

	prompt = ""
	earliest = "8:00"
	latest = "21:00"
	print("Te gustaría incluir sólamente cursos dentro de cierto rango temporal? Ingresar en formato hh:mm separados por un espacio.")
	print("Ejemplo: 10:00 19:00")
	print("Para omitir, ingresa no.")
	while prompt != "no":
		prompt = input()
		if prompt == "no":
			break

		prompt = prompt.split()
		earliest = prompt[0]
		latest = prompt[1]
		prompt = "no"

	sch = Schedule()
	for course in found:
		sch.add_course(course)

	good_courses = solverFindCourse(sch, earliest, latest, db)
	print("Aquí están los cursos que te sirven!!! son "+str(len(good_courses))+".")
	for course in good_courses:
		print(course.name)
	input()


def findSchedule(db):
	dict_of_courses = {} # parte interactiva -----------------------------------
	prompt = ""
	print("Ingresa el código del ramo que deseas incluir en tu horario (sin la sección).")
	print("Para terminar, ingresa ok")
	while prompt != "ok":

		id = input()
		if id == "ok":
			break

		print("Curso agregado.")
		found = db.search(id)
		dict_of_courses[id] = found

	prompt = ""
	earliest = "8:00"
	latest = "21:00"
	print("Te gustaría escoger cursos dentro de cierta hora del día? Ingresar en formato hh:mm separados por un espacio.")
	print("Ejemplo: 10:00 19:00")
	print("Para omitir, ingrese no")
	while prompt != "no":
		prompt = input()
		if prompt == "no":
			break

		prompt = prompt.split()
		earliest = prompt[0]
		latest = prompt[1]
		prompt = "no"

	# parte donde el pc tiene q pensar ------------------------------------------

	print("Calculando horarios...")
	good_schedules = solve(dict_of_courses, earliest, latest)
	if len(good_schedules) == 0:
		print("No te sirve ningún horario :(")
	else:
		print("Aquí están los " + str(len(good_schedules)) + " horarios que te sirven!")
		print("----------------")
		for sch in good_schedules:
			sch.printSchedule()
			print("----------------")
	input()

main()
