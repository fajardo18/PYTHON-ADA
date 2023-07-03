# Variables de tipo primitivo

edad = 35
print(edad)
print(type(edad))

peso = 75.2
print(peso)
print(type(peso))

Edad = True
print(Edad)

Peso = False
print(Peso)

Edad = input()
print("Tu tienes", int(edad), "años")

# Límite de los enteros y los flotantes en python
# int / Integer: Int puede almacenar todos los valores enteros. Este tipo de dato puede ser de cualquier tamaño.
# No hay límite de tamaño.
# float: el flotante incluye todos los valores de punto flotante.
# Tampoco hay restricciones sobre el tamaño de un número de punto flotante.

# 2+4+6+8...2n
# 2n=70 n=70/2 n=35
# n*(n+1)
n = int(input("ingresar numero"))
print((n)*(n+1))