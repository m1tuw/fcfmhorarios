from ramos import *

class Course:
	def __init__(self, name):
		self.name = name # string, ej CC3101-2
		self.lectures = [] # vector de tuplas (dia, inicio, duracion)
		self.recitations = []

	def add_lecture(self, day, start, end): # start + duration in minutes
		self.lectures.append((day, start, end))

	def add_recitation(self, day, start, end): # start + duration in minutes
		self.recitations.append((day, start, end))

	def printCourse(self):
		print(self.name, self.lectures, self.recitations)


class Schedule:
	def __init__(self):
		self.week = [[],[],[],[],[]] # week guarda tuplas (name, start, end, type), estan todos casteados ya, no preocuparse x eso xD

	def add_course(self, course): # add_course(Ramo ramo): agrega el ramo al horario
		name = course.name
		for lecture in course.lectures:
			day, start, end = lecture[0], lecture[1], lecture[2]
			self.week[dayToInt(day)].append([name, timeToMinutes(start), timeToMinutes(end), "lecture"]) #elements in self.week[day]: (name, start, end, type)

		for recitation in course.recitations:
			day, start, end = recitation[0], recitation[1], recitation[2]
			self.week[dayToInt(day)].append([name, timeToMinutes(start), timeToMinutes(end), "recitation"])

	def remove_course(self, name): # ni idea pk esto esta aqui
		for i in range(5):
			for t in self.week[i][:]:
				if(t[0] == name):
					self.week[i].remove(t)

	def count_clashes(self):
		cnt = 0
		for i in range(5):
			cnt += intervalOverlap(self.week[i])
		return cnt 

	# retorna 1 si hay choques y 0 si nop
	def check_clash(self, course):
		for lecture in course.lectures:
			# revisar si no chocan cn nada
			day, start, end = dayToInt(lecture[0]), timeToMinutes(lecture[1]), timeToMinutes(lecture[2])
			for session in self.week[day]:
				start2 = session[1]
				end2 = session[2]
				if start < start2 and end > start2:
					return 1
				if start < end2 and end > end2:
					return 1
				if start >= start2 and end <= end2:
					return 1
		for recitation in course.recitations:
			# revisar si no chocan cn nada
			day, start, end = dayToInt(recitation[0]), timeToMinutes(recitation[1]), timeToMinutes(recitation[2])
			for session in self.week[day]:
				start2 = session[1]
				end2 = session[2]
				if start < start2 and end > start2:
					return 1
				if start < end2 and end > end2:
					return 1
				if start >= start2 and end <= end2:
					return 1
		return 0


	def printSchedule(self):
		# asumiendo no choques
		if self.count_clashes() != 0:
			print("some courses in your schedule clash. please check and try again later")
			return

		days = [[],[],[],[],[]]

		for i in range(5):
			for j in self.week[i]:
				days[i].append(j[0] + ", " + j[3] + ": " + minutesToTime(j[1]) + " - " + minutesToTime(j[2]))

		print("Mon: " + " ".join(days[0]))
		print("Tue: " + " ".join(days[1]))
		print("Wed: " + " ".join(days[2]))
		print("Thu: " + " ".join(days[3]))
		print("Fri: " + " ".join(days[4]))

def loadDB():
	courseList = []
	f = open("db.txt", "r")
	lines = f.readlines()
	names = {}
	for line in lines:
		L = line.split()
		names[L[0][:6]] = L[len(L)-1]
		name = L[0]
		course = Course(name)
		number_of_lectures = int(L[1])
		number_of_recitations = int(L[2])
		for i in range(number_of_lectures):
			j = 3*(i+1)
			day = L[j]
			start = L[j + 1]
			length = L[j + 2]
			course.add_lecture(day, start, length)

		for i in range(number_of_recitations):
			j = 3*(number_of_lectures+i+1)
			day = L[j]
			start = L[j + 1]
			length = L[j + 2]
			course.add_recitation(day, start, length)
		courseList.append(course)
	return (courseList, names)

class Database():
	def __init__(self):
		self.database = [] # database es una lista de cursos
		self.names = {}

	def load(self):
		self.database, self.names = loadDB()

	def search(self, id):
		ret = []
		for course in self.database:
			ind = course.name.index("-")
			if course.name[:ind] == id:
				ret.append(course)
		return ret

	def searchWithSection(self, id):
		for course in self.database:
			if course.name == id:
				return course

	def getName(self, id):
		return self.names[id]
