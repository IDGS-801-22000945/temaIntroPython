'''
 range genera una lista de valores
 # 0, 1, 2.... 19
'''
range(20)

for i in range(20):
    print(i)


range(20)
x=range(10,20)
'''
 hace el recorrido del 0 al 19, pero de 2 en 2
'''
y=range(1,20,2)
for i in range(20):
    print(i)

print("Tabla de multiplicar")
num = int(input("Inserte el número para la tabla: "))
for i in range(11):
    print(f"{i} * {num} = {i * num}")
