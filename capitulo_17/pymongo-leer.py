# -*- coding: utf-8 -*-
"""
Created on Sat Sep  4 22:22:10 2021

@author: zimiz
"""

from pymongo import MongoClient
conexion=MongoClient("mongodb://localhost:27017/")

basedatos=conexion.cine
colecc=basedatos.peliculas
print("La coleccion tiene",colecc.count_documents({}),"documentos.")

peli1=colecc.find_one({"genero":"Drama"})
print("\nPrimera pelicula con genero Drama:\n",peli1)

peli2=colecc.find_one({"genero":"Drama"},
                      {"titulo1":1,"direccion":1})
print("\nSolo la id, titulo y direccion:\n",peli2)

peli3=colecc.find_one({"genero":"Drama"},
                      {"_id":0,"genero":0,"reparto":0})
print("\nTodos los campos menos id, genero y reparto:\n",peli3)

print("\nLas peliculas de comedia son:",end="")
for x in colecc.find({"genero":"Comedia"}):
    print("\n",x["titulo"], "de",x["direccion"])
    print("  reparto:",end=" ")
    for r in x["reparto"]:
        print(r, end=" \n")