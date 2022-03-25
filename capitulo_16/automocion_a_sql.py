import pandas as pd
import os
import sqlite3 as sql

ruta=os.getcwd()+"\\Documents\"
excel=pd.read_excel(ruta+"Listados Excel.xlsx",
sheet_name="Automocion", header=0)

fabric=["nissan","toyota","volvo"]
listado=excel[excel.fabricante.isin(fabric) & excel.tipo_combustible.isin(["gas"])]
tabla=listado.pivot_table(index="carroceria", columns="fabricante",values="consumo_ciudad",fill_value=0).round(2)

print("Tabla pivot:\n", tabla)
conex = sql.connect(ruta + "automocion_tablas.sqlite")
tabla.to_sql("consumos", con = conex, if_exists = "replace", index_label = "carroceria")