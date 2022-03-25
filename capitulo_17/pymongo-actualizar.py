# -*- coding: utf-8 -*-
"""
Created on Sat Sep  4 23:04:08 2021

@author: zimiz
"""

from pymongo import MongoClient
conexion=MongoClient("mongodb://localhost:27017/")

basedatos=conexion.cine
colecc=basedatos.peliculas

def listadouno(tit):
    peli=colecc.find_one({"titulo":tit})
    print(peli["titulo"],peli["año"],peli["direccion"])
    
def listadovarios(lista):
    for peli in lista:
        print(peli["titulo"],peli["año"],peli["direccion"],peli["notas"])
        

result=colecc.update_one({"titulo":"Gothika"},{"$set":{"año":2000}})
print("\nPelicula Gothika con año cambiado(documentos cambiados):",
      result.modified_count)
listadouno("Gothika")

result=colecc.update_one({"titulo":"Gothika"},{"$max":{"año":2003}})
print("\nVolvemos a actualizarla a su año correcto:")
listadouno("Gothika")

result=colecc.update_many({},{"$min":{"año":2020}})
print("\nCualquier pelicula con año superior a 2020 se reduce a 2020. Total cambios:",
      result.modified_count)

colecc.update_many({},{"$set":{"anotaciones":"(sin notas agregadas)"}})
print("\nAgregamos un nuevo campo llamado 'anotaciones' a todos los documentos.")
print("La lista de campos del primer documento es:", colecc.find_one().keys())
colecc.update_many({},{"$rename":{"anotaciones":"notas"}})
print("Lo renombramos a 'notas'. La lista cambiada es:", colecc.find_one().keys())

colecc.update_many({"genero":"Comedia"},
                   {"$set":{"notas":"Hay varios tipos de comedias"}})
print("\nAnotamos en todas las comedias. El resultado:")
listadovarios(colecc.find())