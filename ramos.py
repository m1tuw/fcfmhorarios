def timeToMinutes(s):
	L = s.split(":")
	hh = int(L[0])
	mm = int(L[1])
	return hh*60 + mm

def minutesToTime(n):
	hh = n//60
	mm = n%60
	hh = str(hh)
	mm = str(mm)
	if(len(mm) < 2):
		mm = '0'+mm
	return str(hh)+":"+str(mm)


def dayToInt(s):
	days_dict = {
    'Mon': 0,
    'Tue': 1,
    'Wed': 2,
    'Thu': 3,
    'Fri': 4,
    'Sat': 5,
    'Sun': 6
	}
	return days_dict[s]

def filterNames(L):
	ret = []
	for x in L:
		ret.append([x[1],x[2]])
	return ret

# advertencia!!! no sirve para casos muy brigidos xd no lo planteé como problema progcomp!!!
def intervalOverlap(weekday): # l es una lista de pares (l, r)
	L = filterNames(weekday)
	clashes = 0
	L.sort()
	for i in range(len(L) - 1):
		if L[i][1] > L[i+1][0]:
			clashes += 1
	return clashes

L = [["a",2,4],["b",3,6],["c",7,8],["d",8,10],["e",9,10]]
# tests
assert intervalOverlap(L) == 2

def searchDatabase(name):
	# retorna un vector con ramos
	res = []
	
