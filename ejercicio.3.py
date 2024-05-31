mayores_edad = 0
menores_edad = 0
cantidad_mujeres = 0
cantidad_hombres = 0

for _ in range(15):
    edad = int(input("Ingrese la edad de la persona: "))
    sexo = input("Ingrese el sexo de la persona (M/F): ").upper()

    if edad >= 18:
        mayores_edad += 1
    else:
        menores_edad += 1

    if sexo == "F":
        cantidad_mujeres += 1
    elif sexo == "M":
        cantidad_hombres += 1
    else:
        print("Sexo no válido. Por favor, ingrese 'M' para masculino o 'F' para femenino.")

print(f"La cantidad de mujeres es: {cantidad_mujeres}")
print(f"La cantidad de hombres es: {cantidad_hombres}")
print(f"La cantidad total de menores de edad es: {menores_edad}")
print(f"La cantidad total de mayores de edad es: {mayores_edad}")
