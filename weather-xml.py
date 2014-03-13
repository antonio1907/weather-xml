# -*- coding: utf-8 -*-
import requests
from lxml import etree
from jinja2 import Template
import webbrowser

f = open('plantilla.html','r')



html = ' '

for linea in f:
	html += linea

plantilla = Template(html)

ciudades = ["Almeria","Cadiz","Cordoba","Granada","Huelva","Jaen","Malaga","Sevilla","Dos Hermanas"]
tempe_min = []
tempe_max = []
viento_vel = []
viento_direc = []

for ciudad in ciudades:
	valores = {'q': '%s,spain' % ciudadp,'mode': 'xml','units': 'metric','lang': 'es'}
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
	tempe_min.append(tempemin2)
	tempe_max.append(tempemax2)
	viento_vel.append(viento2)
	viento_direc.append(direccion2)

tiempo = plantilla.render(ciudadp=ciudades,temp_max=tempe_max,temp_min=tempe_min,speed=viento_vel,direccion=viento_direc)
fichero = open('tiempo.html','w')
fichero.write(tiempo)
fichero.close()
webbrowser.open("tiempo.html")	
