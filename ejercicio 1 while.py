# Crea un programa que pida números infinitamente. Los números introducidos deben ser cada vez mayores El programa finalizará cuando se introduce un número menor que el anterior.

num1 = int(input("Entra un número: "))
num2 = int(input("Entra otro número más grande que " + str(num1) + ": "))

while num1 < num2:
    num1 = num2
    num2 = int(input("Entra otro número más grande que " + str(num1) + " :"))

print("Has introducido un numero más pequeño o igual que " + str(num1))
