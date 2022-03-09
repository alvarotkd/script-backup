from datetime import date
import shutil
import os

fecha= date.today()
 
fecha_backup = str(fecha).replace('-','-')

origen= r'D:\Alvaro\\escritorio\\Escritorio\\python\bckup\script-backup\\asd'
destino= r'Z:\\' +'\\' + fecha_backup
archivos = os.listdir(origen)
if os.path.isdir(destino):
    fecha_backup = str(fecha)

for g in archivos:
        shutil.move(origen + g, destino)
    
    

print(" backup realizado")


