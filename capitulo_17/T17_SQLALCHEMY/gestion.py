# -*- coding: utf-8 -*-
"""
Created on Sun Sep  5 11:19:02 2021

@author: zimiz
"""
from modelos import Socio, Compra
from conexion import engine
from sqlalchemy.orm import sessionmaker

def altasocio():
    print("Alta de nuevo socio\n")
    nom = input("Nombre del socio: ")
    tel = input("Teléfono del socio: ")
    nuevo = Socio(nombre = nom, telefono = tel)
    sesion.add(nuevo)
    sesion.commit()


def altacompra():
    print("Nueva Compra")
    num = input("Número de socio que realiza la compra: ")
    socio = sesion.query(Socio).filter(Socio.num == num).scalar()
    if socio:
        print("Compra de", socio.nombre)
        producto = input("Codigo de producto: ")
        total = input("Total de compra: ")
        nueva = Compra(producto=producto, total=total)
        socio.miscompras.append(nueva)
        sesion.commit()
    else:
        print(" El Socio con el numero:", num, "no existe.")
        
def consulta():
    concompras = sesion.query(Socio).join(Compra)
    print("\nCLIENTES CON COMPRAS:")
    for reg in concompras:
        totalf = 0
        print("-----------------------")
        listado = ""
        for com in reg.miscompras:
            listado += "\n  -- Nº factura: {} Total: {}\n".format(
    				com.factura, com.total)
            totalf += com.total
        print("Total facturas de", reg.nombre,": {:.2f}\n".format(totalf), listado)

Session = sessionmaker(bind = engine)
sesion = Session() 


opcion=""

while opcion!="0":
    print("Menu de Opciones".center(40,"-"))
    print("1-Altas de socios")
    print("2-Nuevas compras")
    print("3-Consultas de socios y compras")
    opcion=input("Elija una opcion:")
    if opcion=="1":
        altasocio()
    if opcion=="2":
        altacompra()
    if opcion=="3":
        consulta()
    if opcion=="0":
        quit()