print("ASSIGNATURAS OPTATIVAS")

print("Asignaturas optativas: Informática gráfica - Pruebas de software - Usabilidad y accesibilidad")
asignatura = input("Escribe la asignatura que deseas: ").lower()

if asignatura in ("informática gráfica", "pruebas de software", "usabilidad y accesibilidad"):
    print("Has elegido la assigantura " + asignatura)
else:
    print("Has elegido una assignatura incorrecta")
