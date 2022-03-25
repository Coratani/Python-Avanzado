# -*- coding: utf-8 -*-
"""
Created on Sat Sep  4 21:43:48 2021

@author: zimiz
"""

from pymongo import MongoClient

conexion=MongoClient("mongodb://localhost:27017/")
basedatos=conexion.cine
colecc=basedatos.peliculas

nuevo=colecc.insert_one({"titulo":"La vida es bella",
                         "año":1997,
                         "direccion":"Roberto Benigni",
                         "reparto":["Roberto Benigni","Nicoleta Braschi",
                                    "Marisa Paredes"],
                         "genero":["Comedia","Drama"]})
print("Identificador del nuevo documento:", nuevo.inserted_id)
                        
varias=[{"titulo":"Solas",
         "año":1999,
         "direccion":"Benito Zambrano",
         "genero":"Drama"},
        {"titulo":"Todo es mentira",
                         "año":1994,
                         "direccion":"Alvaro Fernandez Almero",
                         "genero":["Comedia","Romance"],
                         "reparto":["Coque Malla",
                                    "Penelope Cruz",
                                    "Jordi Molla"]}]
dos=colecc.insert_many(varias)
print("Identificadores de nuevos documentos:", dos.inserted_ids)
print("\nColecciones creadas:",basedatos.list_collection_names())