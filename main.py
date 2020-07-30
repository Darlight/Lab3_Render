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
bitmap.glCreateWindow()
print(bitmap.glInit())
bitmap.load('./Models/face.obj', (15,15),(15,10))
bitmap.glFinish('output.bmp')