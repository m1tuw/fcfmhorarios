import re
import colorama
import requests
from bs4 import BeautifulSoup

es_en_weekdays = {
	"Lunes": "Mon",
	"Martes": "Tue",
	"Miércoles": "Wed",
	"Jueves": "Thu",
	"Viernes": "Fri",
	"Sábado": "Sat",
	"Domingo": "Sun"
}

def parse(s1, s2):
    name = s1
    s2 = s2.replace("Laboratorio", "Cátedra")
    s2 = s2.replace("Cátedra:", "Cátedra,")
    s2 = s2.replace("Auxiliar:", "Auxiliar,")
    s2 = s2.split('\n')

    number_of_lectures = 0
    number_of_recitations = 0

    lectures = []
    recitations = []

    for s in s2:
    	parts = s.split(",")
    	for i in range(len(parts)):
    		parts[i] = parts[i].strip()
    	
    	class_type = parts[0]
    	if(class_type == "Cátedra"):
    		for i in range(1, len(parts)):
    			session = parts[i]
    			L = session.split()
    			if L[0] not in es_en_weekdays:
    				break
    			number_of_lectures += 1
    			day = es_en_weekdays[L[0]]
    			start = L[1]
    			end = L[3]
    			lectures.append((day, start, end))

    	if(class_type == "Auxiliar"):
    		for i in range(1, len(parts)):
    			session = parts[i]
    			L = session.split()
    			if L[0] not in es_en_weekdays:
    				break
    			number_of_recitations += 1
    			day = es_en_weekdays[L[0]]
    			start = L[1]
    			end = L[3]
    			recitations.append((day, start, end))

    res = [name, str(number_of_lectures), str(number_of_recitations)]
    for lecture in lectures:
    	res.append(lecture[0])
    	res.append(lecture[1])
    	res.append(lecture[2])

    for recitation in recitations:
    	res.append(recitation[0])
    	res.append(recitation[1])
    	res.append(recitation[2])

    return " ".join(res)

file = open("db.txt", "a")


website = "https://ucampus.uchile.cl/m/fcfm_catalogo/?semestre=20241&depto=9" # cambiar esto para sacar cursos d otros lados
response = requests.get(website)

if response.status_code != 200:
	print("No se ha podido obtener la información del URL: ", response.status_code)

else:
	soup = BeautifulSoup(response.content, "html.parser")
	#print(soup.title.children)
	cursos_class = soup.find_all(class_="cursos")
	for cursos in cursos_class:
		tr_elements = cursos.find_all("tr")
		for tr in tr_elements:
			if(tr.get("id") != None):
				# now find last td
				td_elements = tr.find_all("td")
				ultimo = td_elements[len(td_elements) - 1]
				div_elements = ultimo.find_all("div")
				for div in div_elements:
					if(div.get("title") != None):
						s1 = str(tr.get("id"))
						s2 = str(div.get("title"))
						#print(parse(s1, s2))
						file.write(parse(s1, s2))
						file.write('\n')

file.close()
