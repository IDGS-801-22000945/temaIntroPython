def funcion1():
    print("Hola, soy la función 1")

def funcion2():
      print("Hola, soy la función 2")


def run():
     funcion1()
     funcion2()

run()    

def funcion1():
     print("Hola soy la funcion 1")

def funcion2():
     print("Hola soy la funcion 2")


import os

def funcion1():
     os.system("cls")
     num1=int(input('Numero1: '))
     num2=int(input('Numero2: '))
     res=num1+num2
     print(f'Resultado: {res}')
     input("")

def funcion2():
     os.system("cls")
     num1=int(input('Numero1: '))
     num2=int(input('Numero2: '))
     res=num1-num2
     print(f'Resultado: {res}')
     input("")

def funcion3():
     os.system("cls")
     num1=int(input('Numero1: '))
     num2=int(input('Numero2: '))
     res=num1*num2
     print(f'Resultado: {res}')
     input("")

def funcion4():
     os.system("cls")
     num1=int(input('Numero1: '))
     num2=int(input('Numero2: '))
     res=num1*num2
     print(f'Resultado: {res}')
     input("")

def run():
    while True:
     os.system('cls')
     print('1. Suma')
     print('2. Resta')
     print('3. Multiplicacion')
     print('4. Division')
     print('5. Salir')
     op=int(input('Opcion: '))
     if op==1:
          funcion1()
     if op==2:
          funcion2()
     if op==3:
         funcion3()
     if op==4:
         funcion4()
     if op==5:
         break
    



if __name__ == "__main__":
     run()

