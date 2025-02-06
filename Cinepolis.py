'''
Jaqueline Núñez Mendoza
IDGS801
'''

import os
from io import open

class CineBoletos:
    def __init__(self):
        self.ventas = [] 
        archivo = open("ventas.txt", "w")
        archivo.write("") 
        archivo.close()

    def comprar_boletos(self):
        os.system("cls")
        nombre = input("Escriba su nombre: ")
        numPersonas = int(input("Escriba el número de acompañantes: "))
        numBoletos = int(input("Escriba el número de boletos que desea comprar: "))

        while numBoletos > (numPersonas) * 7:  
            print(f"No puedes comprar más de {(numPersonas) * 7} boletos para {numPersonas} personas.")
            print("¿Desea modificar el número de acompañantes o de boletos?")
            print("1. Cambiar número de acompañantes.")
            print("2. Cambiar número de boletos.")
            opcion = int(input("Seleccione una opción: "))
            if opcion == 1:
                numAdicional = int(input("Ingrese el número adicional de acompañantes: "))
                numPersonas += numAdicional
            if opcion == 2:
                numBoletos = int(input("Ingrese el nuevo número de boletos que desea comprar: "))
          
        print("Método de pago:")
        print("1. Pago en Efectivo")
        print("2. Pago con tarjeta CINECO (10% de descuento adicional)")
        metodoPago = int(input("Seleccione una opción: "))
        precioBoleto = 12
        total = numBoletos * precioBoleto
        
        descuento = 0
        if 3<= numBoletos <=5:
            descuento= total * 0.1
        if numBoletos > 5:
            descuento = total * 0.15
        total -= descuento

        if metodoPago == 1:
            print(f"Total: {total:.2f}")
        if metodoPago == 2:
            descuentoTarjeta = total * 0.1
            total -= descuentoTarjeta
            print(f"Descuento aplicado: ${descuentoTarjeta:.2f}")
            print(f"Total a pagar: ${total:.2f}")

        self.ventas.append((nombre, total)) 

        archivo=open("ventas.txt","a")
        archivo.write(f"{nombre} - Total: ${total:.2f}\n")
        print("Venta registrada con éxito.")

    def corteVenta(self):
        os.system("cls")
        print("Corte de ventas")
        # <20 y <10 son parametros de espaciado, en este caso los utilice para espaciar a la izquierda
        print(f"{'Nombre':<20}{'Total':<10}")
        print("-" * 30)
        totalGeneral = 0

 
        archivo=open("ventas.txt","r")
        for i in archivo:
            #Strip elimina espacios al principio y final
            print(i.strip())
            # split divide la línea en dos partes, el separador es "- Total: " en este caso
            _, total_str = i.split("- Total: $")
            totalGeneral += float(total_str)

        print("-" * 30)
        print(f"Total General: ${totalGeneral:.2f}")
        archivo.close()

    def menu(self):
        while True:
            os.system("cls")
            print("Menú Principal")
            print("1. Comprar boletos")
            print("2. Terminar")
            opcion = int(input("Elige una opción: "))
            
            if opcion == 1:
                self.comprar_boletos()
            if opcion == 2:
                self.corteVenta()
                print("Gracias por usar el sistema. Hasta luego.")
                break
            else:
                input("\nPresiona Enter para continuar...")

if __name__ == "__main__":
    cine = CineBoletos()
    cine.menu()