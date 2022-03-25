# -*- coding: utf-8 -*-
"""
Created on Sun Sep  5 11:04:13 2021

@author: zimiz
"""

from conexion import engine
from sqlalchemy import Column, Integer, String, Float, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

base = declarative_base()

class Socio(base):
    __tablename__ = "socios"
    num = Column(Integer, primary_key=True)
    nombre = Column(String)
    telefono = Column(String)

class Compra(base):
   __tablename__ = "compras"
   factura = Column(Integer, primary_key = True)
   num_socio = Column(Integer, ForeignKey("socios.num"))
   producto = Column(String)
   total = Column(Float)

Socio.miscompras = relationship("Compra", order_by = Compra.factura,
             backref="socios", cascade="all, delete-orphan")

base.metadata.create_all(engine)