# -*- coding: utf-8 -*-
"""
Created on Sat Aug 28 17:51:41 2021

@author: zimiz
"""

import numpy as np

elementos = np.array([["materia","mercado","natural"]])
prefijos=np.array([["anti","super","des"]])

print("Podemos anyadir los elementos de un array en los de otro:\n",
      np.char.add(prefijos, elementos))
print("y tambien anyadir un prefijo a todos los elementos:\n",
      np.char.add("super", elementos))

sonidos=np.array(["riing! ","chof! ","plas! "])
print("Repetimos tres veces el contenido de un array:\n",
      np.char.multiply(sonidos, 3))

print("Centramos cada elemento con caracteres de relleno:\n",
      np.char.center(elementos, 20,"*"))
frases=np.array(["  El dinero es importante  ",
                 "  y tengo dinero  ",
                 "  necesito dinero  "])
print("Eliminamos espacios de este array:\n", frases, "\n",
      np.char.strip(frases))
frases2=np.char.strip(frases," o y")
print("incluso podemos eliminar mas caracteres (o, espacio, y):\n", frases2)
print("Para anyadir algunos sufijos:",
      np.char.add(frases2, ["!","ito","ales"]))
print("Incluso cambiar palabras completas por otras:\n",
      np.char.strip(np.char.replace(frases, "dinero", "amor")))

codif=np.char.encode(elementos, "cp500")
print("Un array codificado:\n", codif)
decodif=np.char.decode(codif,"cp500")
print("y despues descodificado:\n", decodif)
