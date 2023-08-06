correo = input("Entra aquí tu correo electrónico: ")

if correo.count("@")==1 and correo.index("@")!=0 and correo.index("@")!=len(correo)-1:
    print("El correo es correcto")
else:
    print(("El correo es incorrecto"))

