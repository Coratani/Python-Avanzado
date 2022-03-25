# -*- coding: utf-8 -*-
"""
Created on Sat Sep  4 23:22:01 2021

@author: zimiz
"""


from pymongo import MongoClient
conexion=MongoClient("mongodb://localhost:27017/")

basedatos=conexion.cine
colecc=basedatos.peliculas

result=colecc.delete_many({"genero":"Accion"})
print("\nSe han borrado las peliculas de accion, en total", result.deleted_count)

result=colecc.delete_many({"genero":{"$in":["Secuela","Terror"]}})
print("Se han borrado las peliculas de terror y las secuelas, en total",
      result.deleted_count)
print("La coleccion tiene", colecc.count_documents({}),"documentos.")