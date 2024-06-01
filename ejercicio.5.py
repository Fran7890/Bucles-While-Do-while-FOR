
#Leer 15 números negativos y convertirlos a positivos e imprimir dichos números.
numero_negativo=[]
numero=0
for numero in range(15):
    numero=int(input("ingrese el numero negativo deseado:"))
    if numero < 0:
        numero_negativo.append(abs(numero))
        

#resultado del ejercicio 
print(f"el resultado de los numeros negativos convertidos en positivos  son : {numero_negativo}")
