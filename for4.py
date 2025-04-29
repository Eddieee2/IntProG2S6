numero = int(input("Ingrese un numero para generar sus tablas de multiplicacion: "))

print(f"Tablas de multiplicar del numero {numero}:")
for i in range(1, 13):
    print(f"{numero} x {i} = {numero * i}")