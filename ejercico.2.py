#Leer 10 números y obtener la cantidad de mayores y la cantidad de menores a 100, cuál es el número máximo y cuál es el número mínimo.
# Inicializar listas y variables
numeros = []
mayores_100 = 0
menores_100 = 0
numero_maximo = None
numero_minimo = None

# Leer 10 números
print("Introduce 10 números:")
for i in range(10):
    numero = float(input(f"Número {i+1}: "))
    numeros.append(numero)

# Procesar los números
for numero in numeros:
    if numero > 100:
        mayores_100 += 1
    elif numero < 100:
        menores_100 += 1
    
    if numero_maximo is None or numero > numero_maximo:
        numero_maximo = numero
    
    if numero_minimo is None or numero < numero_minimo:
        numero_minimo = numero

# Mostrar resultados
print(f"Cantidad de números mayores a 100: {mayores_100}")
print(f"Cantidad de números menores a 100: {menores_100}")
print(f"El número máximo es: {numero_maximo}")
print(f"El número mínimo es: {numero_minimo}")
