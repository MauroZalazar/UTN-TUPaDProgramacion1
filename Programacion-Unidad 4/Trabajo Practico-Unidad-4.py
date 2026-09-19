#Punto 1

for i in range(101):
    print(i)

#Punto 2

num = int(input("Ingrese un número entero: "))
contador = 0
numero_temporal = abs(num)

if numero_temporal == 0:
    contador = 1
else:
    while numero_temporal > 0:
        numero_temporal //= 10
        contador += 1
        
print(f"El número tiene {contador} dígitos.")

#Punto 3

a = int(input("Ingrese el primer valor: "))
b = int(input("Ingrese el segundo valor: "))

inicio = min(a, b) + 1
fin = max(a, b)
suma = 0

for i in range(inicio, fin):
    suma += i

print(f"La suma es: {suma}")

#Punto 4

suma = 0
numero = int(input("Ingrese un número (0 para terminar): "))

while numero != 0:
    suma += numero
    numero = int(input("Ingrese otro número (0 para terminar): "))

print(f"Total acumulado: {suma}")

#Punto 5

import random
secreto = random.randint(0, 9)
intentos = 0
adivinado = False

while not adivinado:
    intento = int(input("Adivina el número (0 al 9): "))
    intentos += 1
    if intento == secreto:
        adivinado = True
    else:
        print("¡Incorrecto! Intenta de nuevo.")

print(f"¡Acertaste! Te tomó {intentos} intentos.")

#Punto 6

for i in range(100, -1, -2):
    print(i)

#Punto 7

n = int(input("Ingrese un número entero positivo: "))
suma = 0

for i in range(n + 1):
    suma += i

print(f"La suma de 0 hasta {n} es: {suma}")

#Punto 8

cantidad = 5 
pares = impares = positivos = negativos = 0

for _ in range(cantidad):
    num = int(input("Ingrese un número entero: "))
    if num > 0:
        positivos += 1
    elif num < 0:
        negativos += 1

    if num % 2 == 0:
        pares += 1
    else:
        impares += 1

print(f"Pares: {pares}, Impares: {impares}, Positivos: {positivos}, Negativos: {negativos}")

#Punto 9

cantidad = 5  
suma = 0

for _ in range(cantidad):
    num = float(input("Ingrese un número: "))
    suma += num

media = suma / cantidad
print(f"La media de los valores es: {media}")

#Punto 10

numero = int(input("Ingrese un número: "))
invertido = 0
copia_numero = numero

while copia_numero > 0:
    digito = copia_numero % 10                
    invertido = (invertido * 10) + digito 
    copia_numero //= 10                       
      
print(f"Número invertido: {invertido}")