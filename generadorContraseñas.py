import random

print("\nBienvenido a tu generador de contraseñas de confianza :)\n")
print("1. Generar una contraseña aleatoria\n2. Accede a la configuración de contraseñas")
r = input("\nElije, ¿1 o 2? ")


if r == "1":
    unonueve = "123456789"
    aleatorio = random.choice(unonueve)
    aleatorio = int(aleatorio)
    largo = 7 + aleatorio

    caracteres = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!?,.-:;+()$&"

    contraseña = ""

    for i in range(largo):
        contraseña += random.choice(caracteres)

    print("\nAquí tienes tu contraseña aleatoria:\n"+contraseña+"\n")

elif r == "2":
    numContras = input("\nCuantas contraseñas quieres crear? ")
    numContras = int(numContras)
    numCaracteres = input("De cuantos caracteres quieres que sean la/s contraseñas? ")
    numCaracteres = int(numCaracteres)

    caracteres = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!?,.-:;+()$&"

    contraseña = ""
    cont = 1
    for i in range(numContras):
        
        for o in range(numCaracteres):
            contraseña += random.choice(caracteres)
            
            if len(contraseña.replace("\n", "")) == (numCaracteres * cont):
                cont += 1
                contraseña += "\n"

    if numContras == 1:
        print("\nAquí tienes tu contraseña personalizada:\n"+contraseña+"\n")
    if numContras > 1:
        print("\nAquí tienes tus contraseñas personalizadas:\n"+contraseña+"\n")

else:
    print("Has introducido un valor incorrecto. Vuelve a intentarlo")


#num = input("Indique cuantas contraseñas desea crear: ")
# largo = input("De cuantos caracteres quieres que ses la contraseña? ")
# largo = int(largo)

# caracteres = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!?,.-:;+()$&"

# contraseña = ""

# for i in range(largo):
#     contraseña += random.choice(caracteres)

# print(contraseña)