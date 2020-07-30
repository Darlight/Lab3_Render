"""
Universidad del Valle de Guatemala
Gráficas por computadora
Seccion 10
Lic. Dennis Aldana
Mario Perdomo
18029

main.py
Proposito: Mostrar el modelo 3D
"""

from tezt import Render
from obj import Obj 

bitmap = Render()
print(bitmap.glInit)
bitmap.glCreateWindow()
bitmap.load('./Zack.obj', (0,0),(10,10))

bitmap.glFinish('output.bmp')