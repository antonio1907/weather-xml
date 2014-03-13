
import requests
from lxml import etree
from jinja2 import Template
import webbrowser

f = open('plantilla.html','r')



html = ' '

for linea in f:
	html += linea

plantilla = Template(html)

ciudades = ["Almeria","Cadiz","Cordoba","Granada","Huelva","Jaen","Malaga","Sevilla"]
temperatura_min = []
temperatura_max = []
velocidad_viento = []
direccion_viento = []

for ciudad in ciudades:
	valores = {'q': '%s,spain' % ciudad,'mode': 'xml','units': 'metric','lang': 'es'}
	respuesta = requests.get('http://api.openweathermap.org/data/2.5/weather',params=valores)

	raiz = etree.fromstring(respuesta.text.encode("utf-8"))	

	city = raiz.find("city")
	city.attrib["name"]
	tempemin = raiz.find("temperature")
	tempemin2 = round(float(tempemin.attrib["min"]),1)
	tempemax = raiz.find("temperature")
	tempemax2 = round(float(tempemax.attrib["max"]),1)
	viento = raiz.find("wind/speed")
	viento2 = round(float(viento.attrib["value"]),1)
	direccion = raiz.find("wind/direction")
	direccion2 = direccion.attrib["code"]
	temperatura_min.append(tempemin2)
	temperatura_max.append(tempemax2)
	velocidad_viento.append(viento2)
	direccion_viento.append(direccion2)

tiempo = plantilla.render(ciudad=ciudades,temp_max=temperatura_max,temp_min=temperatura_min,speed=velocidad_viento,direccion=direccion_viento)
fichero = open('tiempo.html','w')
fichero.write(tiempo)
fichero.close()
webbrowser.open("tiempo.html")	
