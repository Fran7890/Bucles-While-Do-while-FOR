#Leer 10 números y mostrar solamente los números positivos, y su sumatoria.
numero=0
numeros_positivos=[]
suma_positivo=0
for numero  in range(  10):
    numero=int(input("ingrese el numero deseado : "))
    if  numero >0:
        numeros_positivos.append (numero)
        suma_positivo += numero 
    


#resultado del ejercicio 
print(f"los numeros positivos son {numeros_positivos}: ")
print(f" el resultado de la suma total de numeros positivos es : {suma_positivo}")