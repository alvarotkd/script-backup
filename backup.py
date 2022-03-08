from datetime import date
import shutil

fecha= date.today()
 
fecha_backup = str(fecha).replace('-','-')

origen= r''
destino= r''+'\\'+fecha_backup 

shutil.copytree (origen,destino)



