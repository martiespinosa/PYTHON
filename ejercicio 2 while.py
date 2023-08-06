# Crea un programa que pida números positivos indefinidamente. El programa termina cuando se introduce un número negativo. Finalmente el programa muestras la suma de todos los números introducidos

i = 0
num = int(input("Entra un número positivo: "))

while num > 0:
    i = i + num
    print("La suma es igual a: " + str(i))
    num = int(input("Entra otro número positivo: "))

if num < 0:
    print("Has introducido un número negativo")
    print("La suma de todos los numeros positivos que has introducido es: " + str(i))