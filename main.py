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
from pathlib import Path
from tezt import Render
from obj import Obj 
import os

#data_folder = Path("Users/MarioAndres/Documents/GitHub/Lab3_Render/Models")

#file_to_open = data_folder / "wario.obj"

#f = open(file_to_open)

#print(f.read())

cwd = os.getcwd()

#print(cwd)
dir_path = os.path.dirname(os.path.realpath( __file__))
model_path = os.path.join(dir_path, r'Models\face.obj')
print(model_path)

bitmap = Render()
bitmap.glCreateWindow()
print(bitmap.glInit())
bitmap.load(model_path, (10,10),(5,5))
bitmap.glFinish('output.bmp')