import os
import re

textosEncontrados = []
nombre = input("ingresar el nombre del archivo:")
listaBusqueda = ['error','falla']
listaFiltros = ['errors']
expRegHora= "\d{2}:\d{2}:\d{2}"
expRebFecha= "\d{4}-\d{2}-\d{2}"
listaBusqueda.append(expRegHora)
listaBusqueda.append(expRebFecha)
def cantidadPalabras(frase):
    palabras = frase.split(" ");
    print(f" cantidad: {len(palabras)} lista palabras: {palabras} frase: {frase}")

def estaPalabra(listaBusqueda,frase):
	matchea = False
	for palabra in listaBusqueda:
		patron = re.compile(palabra.lower())
		match = patron.search(frase.lower())
		if match:
			#print(f" frase con {palabra}: {frase}")
			matchea = True
	return matchea

def estaTodaLaLista(listaBusqueda,frase):
	for palabra in listaBusqueda:
		patron = re.compile(palabra.lower())
		match = patron.search(frase.lower())
		if match:
			continue
		else:
			return False
	return True

def mostrarLista(textos):
	for linea in textos:
		print(f"{linea}")

nombre = "/home/ricardo/Documentos/bitacora/"+nombre
if os.path.isfile(nombre):
	archivo = open(nombre,"r")
	for linea in archivo.readlines():
		# cantidadPalabras(linea)
		if estaPalabra(listaFiltros,linea):
			continue
		if estaTodaLaLista(listaBusqueda, linea):
			print(f"texto tiene las palabras de la lista ordenada: {linea}")
			textosEncontrados.append(linea.strip())
		else:
			if estaPalabra(listaBusqueda, linea):
				textosEncontrados.append(linea.strip())
	archivo.close()
	mostrarLista(textosEncontrados)
else:
	print(f"no se encuentra el archivo:  {nombre}")


