import shutil
import os


origen= r'D:\\prueba'
destino= r'D:\\asd' 
archivos = os.listdir(origen)
for g in archivos:
        shutil.move(origen +'\\'+ g, destino)
    
print(" backup realizado")



