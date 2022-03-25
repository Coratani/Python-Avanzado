# -*- coding: utf-8 -*-
"""
Created on Fri Aug 27 12:20:00 2021

@author: zimiz
"""

import numpy as np
precios = [30.55, 48, 25.85, 45.25, 53]
arrayprecios = np.array(precios)
arrayvalores = np.array(['Juan',45,'Ana',37,'Carmen',53])
print('precios:', arrayprecios)
print('nombres y edades:', arrayvalores)
incremento = arrayprecios+50
coniva = arrayprecios*0.21
print("Los precios incrementados en 50 son: ",incremento)
print("El IVA de 21% que corresponde a cada precio es :", coniva)
print("El precio final es: ", arrayprecios+coniva)

print("\n","Ejemplos de matrices".center(80,"-"),"\n")
alturas= np.array([[1.65, 1.82, 1.54],[1.92, 1.7, 1.33],[1.63, 1.84, 1.41]])
print("Alturas de diversas personas: \n", alturas)
print("Alturas de la segunda persona de la primera fila:", alturas[0,1])
print("Alturas de la segunda fila: ", alturas[1,:])
print("Alturas de la ultima fila: ",alturas[-1:])
print("Alturas de la tercera columna:", alturas[:,2])
print("Alturas de las dos primeras filas:\n:",alturas[0:2,:])
print("Alturas de la segunda y tercera columnas:\n", alturas[:,1:3])
print("\n","Modificacion de matrices".center(80,"-"),"\n")
encentimetros = alturas*100
print("Las alturas en centimetros son:\n", alturas)
alturas*=2
print("Multiplicamos por 2 todos los valores:\n", alturas)
alturas[1,:]=0
print("Dejamos a 0 las alturas de la segunda fila:\n",alturas)
alturas[:,1]=0
print("Tambien las de la segunda columna:\n", alturas)