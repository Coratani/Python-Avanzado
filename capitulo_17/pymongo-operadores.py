# -*- coding: utf-8 -*-
"""
Created on Sat Sep  4 22:37:29 2021

@author: zimiz
"""

from pymongo import MongoClient
conexion=MongoClient("mongodb://localhost:27017/")

basedatos=conexion.cine
colecc=basedatos.peliculas


def listado(lista):
    for peli in lista:
        print(peli["titulo"],peli["año"],peli["direccion"])
    
if colecc.count_documents({"titulo":"Gothika"})==0:
    colecc.insert_one({"titulo":"Gothika",
                       "año":2003,
                       "direccion":"Mathieu Kassovitz",
                       "reparto":["Halle Berry",
                                  "Bernard Hill",
                                  "Penelope Cruz"],
                       "genero":["Thriller","Terror"]})    
    
if colecc.count_documents({"titulo":"El caballero oscuro"})==0:
    colecc.insert_one({"titulo":"El caballero oscuro",
                       "año":2008,
                       "direccion":"Christopher Nolan",
                       "reparto":["Christian Bale",
                                  "Heath Ledger",
                                  "Michael Caine",
                                  "Morgan Freeman"],
                       "genero":["Comic","Secuela"]}) 
    
print("La coleccion tiene", colecc.count_documents({}),"documentos.")

print("\nPeliculas del siglo XXI:")
listado(colecc.find({"año":{"$gte":2000}}))

print("\nPeliculas con genero comedia o terror:")
listado(colecc.find({"genero":{"$in":["Comedia","Terror"]}}))

print("\nLo mismo, pero ademas del siglo XXI:")
listado(colecc.find({"genero":{"$in":["Comedia","Terror"]},
                     "año":{"$gte":2000}}))

print("\nPeliculas que no sean Drama:")
listado(colecc.find({"genero":{"$ne":["Drama"]}}))

print("\nPeliculas que no sean ni comedia ni de Penelope Cruz:")
listado(colecc.find({"genero":{"$ne":"Comedia"},
                     "reparto":{"$ne":"Penelope Cruz"}}))