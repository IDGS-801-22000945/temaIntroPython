
from io import open
import math

#letra a, para que agregue, se vaya añadiendo
#letra w, sobrescribe
#Letra r, lee
#readline solo lee la primera linea, readlines lista (cada una de las líneas del archivo)
#type lee el tipo de variable, solo una parte del archivo
lectura=""
texto=open("archivo.txt","r")
lectura= texto.readlines() 
print(lectura)
for i in lectura:
    print(i)
#texto.write("Hola, soy un archivo de texto\n")
#texto.write("Hola, mundo3\n")
texto.close()

