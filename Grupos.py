#!/usr/bin/env python
# -*- coding: utf-8 -*-

import random, grip, pdfkit, csv
from datetime import datetime
import sys

DEFAULT_NAME = 'grupos-'+datetime.now().strftime('%d-%m-%Y')

def main(cantidad=3, filename='lista.csv', new_file=DEFAULT_NAME, ):
	alumnos = read_csv(filename)
	cantidad = int(cantidad)
	cantidad_grupo = len(alumnos)/cantidad
	rest_grupo = len(alumnos)%cantidad
	grupos = make_groups(alumnos, cantidad, cantidad_grupo, rest_grupo)
	make_md(grupos, cantidad_grupo, new_file)
	bake(new_file)


def read_csv(filename='lista.csv'):
	ifile = open(filename, "r")
	reader = csv.reader(ifile, delimiter=";")
	row_num = 0
	array = []
	for row in reader:
		array.append(row)
		row_num += 1
	ifile.close()
	return array

def make_groups(alumnos, cantidad, cantidad_grupo, rest_grupo):
	grupos = []
	for j in range(cantidad_grupo):
		grupo = []
		for i in range(cantidad):
			pos = random.choice(alumnos)
			alumnos.remove(pos)
			grupo.append(pos[0])
		print grupo
		print '------------------------'
		grupo[0] = '**' + str(grupo[0]) + '**'
		grupos.append(grupo)
	for i in range(rest_grupo):
		pos = random.choice(alumnos)
		alumnos.remove(pos)
		grupos[i].append(pos[0])

	print '------------------------'
	print grupos
	print alumnos
	return grupos

def make_md(grupos, cantidad_grupo, filename):
	archivo = open(filename+'.md', 'w')
	archivo.write('# Grupos ' + datetime.now().strftime('%d-%m-%Y') + '\n')
	for numero_grupo in range(cantidad_grupo):
		cabecera = '### Grupo {}'.format(numero_grupo+1)
		archivo.write(cabecera)
		for alumno in grupos[numero_grupo]:
			archivo.write('\n - ')
			archivo.write(str(alumno))
		archivo.write('\n')
	archivo.close()

def bake(filename):
	grip.export(path=filename+'.md')
	options = {
	    'page-size': 'A4',
	    'margin-top': '0.75in',
	    'margin-right': '0.75in',
	    'margin-bottom': '0.75in',
	    'margin-left': '0.75in',
	}
	pdfkit.from_file(filename+'.html', filename+'.pdf', options=options)

if __name__ == '__main__':
	args = tuple(sys.argv[1:])
	if len(args) <= 3:
		main(*args)
	else:
		print "Hay argumantos de mas!!"
		print "python Grupos.py <cantidad_por_grupo> <nombre_archivo_lectura> <nombre_archivo_generado>"
