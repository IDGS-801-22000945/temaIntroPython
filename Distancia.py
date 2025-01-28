import math

# x1= -4, y1 = -3 
# x2= 2, y2 = 5

class distPuntos:
 
   def distancia(self):
       self.x1=int(input("Ingrese el valor de x1: "))
       self.y1=int(input("Ingrese el valor de y1: "))
       self.x2=int(input("Ingrese el valor de x2: "))
       self.y2=int(input("Ingrese el valor de y2: "))

       self.result = math.sqrt((self.x2 - self.x1)**2 + (self.y2 - self.y1)**2)
       print("El resultado es: {}".format(self.result))


def main():
   obj=distPuntos()
   obj.distancia()

if __name__ == "__main__":
   main()

  
  