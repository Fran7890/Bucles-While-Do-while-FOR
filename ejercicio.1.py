1#.realice un programa que lea 4 números y diga cuántos son pares y cuantos impares y devuelva la sumatoria de los pares.
# Inicializamos las variables para contar los pares, impares y la suma de pares
count_pares = 0
count_impares = 0
suma_pares = 0

# Leemos 4 números del usuario
numeros = []
for i in range(4):
    numero = int(input(f"Ingrese el número {i+1}: "))
    numeros.append(numero)

# Procesamos cada número
for numero in numeros:
    if numero % 2 == 0:
        count_pares += 1
        suma_pares += numero
    else:
        count_impares += 1

# Mostramos los resultados
print(f"Cantidad de números pares: {count_pares}")
print(f"Cantidad de números impares: count_impares{}")
print(f"Sumatoria de los números pares: {suma_pares}")