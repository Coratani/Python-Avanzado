# -*- coding: utf-8 -*-
"""
Created on Sun Sep  5 12:21:03 2021

@author: zimiz
"""
from pymongo import MongoClient
conexion=MongoClient("mongodb://localhost:27017/")
basedatos=conexion.ejercicio
colecc=basedatos.animales

def nuevo_animal():
    tipo = input("Tipo de animal: ")
    diccio = {"tipo": tipo}
    fin = ""
    while fin != "n":
        campo = input("Nombre del campo: ")
        valor = input("Valor para " + campo + ": ")
        fin = input("Añadir otro campo? ('n' para salir) ")
        diccio[campo]=valor
    nuevo = colecc.insert_one(diccio)
    print(tipo, "Agregado. Identificador del nuevo documento:", nuevo.inserted_id)

def lista_animal():
     tipo = input("Tipo de animal: ")
     result = colecc.find_one({"tipo": tipo})
     if result:
         for animal in colecc.find({"tipo": tipo},{"_id":0, "tipo": 0}):
             print("-".center(40, "-"))
             for dato in animal.items():
                 print((dato[0]+":").ljust(15), dato[1])
     else:
        print("El animal de tipo", tipo,"no existe en la base de datos.")
    
def consulta():
    campo = input("Nombre del campo: ")
    valor = input("Valor para " + campo + ": ")
    result = colecc.find_one({campo: valor})
    if result:
        for animal in colecc.find({campo: valor},{"_id":0,campo:0}):
            print("-".center(40, "-"))
            for dato in animal.items():
                print((dato[0]+":").ljust(15), dato[1])
    else:
        print("El campo '", campo,"' con valor '", valor, "' no se ha encontrado.")
    
    
    
opcion=""
while opcion!="0":
    print("Menu de Opciones".center(40,"-"))
    print("1-Agregar animal")
    print("2-Listado animales")
    print("3-Consultas")
    print("0-Salir")
    opcion=input("Elija una opcion:")
    if opcion=="1":
        nuevo_animal()
    if opcion=="2":
        lista_animal()
    if opcion=="3":
        consulta()
    if opcion=="0":
        quit()