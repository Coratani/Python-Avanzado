# -*- coding: utf-8 -*-
"""
Created on Fri Aug 27 12:49:42 2021

@author: zimiz
"""

import numpy as np

arrceros = np.zeros((4,3), dtype=int)
print("Array con 4 filas y 3 columnas de ceros:\n",arrceros)
arrunos = np.ones((4,3))
print("Array con 4 filas y 3 columnas de unos:\n",arrunos)
arranys= np.arange(1970, 2030, 5)
print("Array con los años de 1970 a 2030, de 5 en 5:\n", arranys)
print("Redimensionado de 3 en 3:\n",np.reshape(arranys,(3,4)))
print("Redimensionado de 3 en 3 por columnas:\n", np.reshape(arranys, (3,4),order="F"))
print("Dimensiones del array de ceros:", arrceros.shape)
arrunidos= np.concatenate((arrceros,arrunos))
print("Arrays de ceros y unos concatenados:\n", arrunidos)
arrpermut = np.transpose(arrunidos)
print("El mismo array con dimensiones intercambiadas:\n",arrpermut)
print("Es lo mismo que: \n", arrunidos.T)   
##########################################################   
print("\n","Ejemplos II".center(50,"-"))
arr50a100, avance = np.linspace(50, 100, 9, retstep=True)
print("Con un avance de", avance, "entre 50 y 100 se genera:\n", arr50a100)
arr50y80, avance2 = np.linspace((50, 80),(100, 150),15, retstep=True)
print("\nCon un avance de", avance2[0], "y", avance2[1],
      " de 50 a 100 y de 80 a 150 se genera:\n", arr50y80)
#restamos 1 a la posicion que indicamos por que los arrays comienzan en 0
print("La quinta posicion de este array es:", arr50y80.flat[4])
print("Este array como vector seria: \n", np.ravel(arr50y80))
arrvotos = np.random.rand(3,2)
print("Array al azar:\n", arrvotos)
arrmasvotos = np.resize(arrvotos, (10,3))
print("Podemos repetir los valores:\n", arrmasvotos)
##############################################################
print("\n", "Ejemplos III".center(50,"-"))
arredades = np.array([[25,33,12],[42,12,63],[12,25,42]])
print("Array con 3 filas y 3 columnas con edades:\n", arredades)
print("Si se anyade una fila mas se convierte en vector:\n",
      np.append(arredades,[[14,42,34]]))
arredades = np.append(arredades,[[14,42,34]], axis=0)
print("Pero indicando 0 en axis conserva las dimensiones:\n", arredades)
print("Se puede insertar un valor y convertir en vector:\n", np.insert(arredades, 5, 900))
arredades= np.insert(arredades,(1,3),900,axis=0)
print("O bien insertarlo en filas...:\n", arredades)
arredades=np.insert(arredades,(1,3),1000, axis=1)
print("...y en columnas:\n", arredades)
arredades=np.delete(arredades,(1,4), axis=1)
print("De forma similar se pueden eliminar columnas..:\n", arredades)
arredades=np.delete(arredades,(1,4),axis=0)
print("...y filas:\n", arredades)
print("Las edades utilizadas en el array, sin repetir y ordenadas:\n",
      np.unique(arredades))
print("Mostrando las filas unicas, aprovechando que se ordenan,\n",
      "comprobamos que el orden de la primera fila afecta a las columnas\n",
      "en el resto de filas, de forma que las columnas se mantengan:\n",
      np.unique(arredades, axis=1))
edades, veces = np.unique(arredades, return_counts=True)
print("Las veces que se repite cada edad:\n", edades, veces)
for edad, vez in zip(edades, veces):
    print(edad,"--->",vez,"vez." if vez==1 else "veces")