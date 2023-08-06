edad = int(input("Introduce tu edad: "))

while edad < 0:
    edad = int(input("Has introducido una edad negativa, introduce tu edad correcta: "))

print("Edad correcta, " + str(edad))
