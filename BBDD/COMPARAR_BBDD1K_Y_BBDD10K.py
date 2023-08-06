from sqlite3 import *

miConexion1 = connect(r"C:\Users\MARTI\Desktop\PYTHON\BBDD\WORDS_WORDLE_1K")
miConexion2 = connect(r"C:\Users\MARTI\Desktop\PYTHON\BBDD\WORDS_WORDLE_10K")

miCursor1 = miConexion1.cursor()
miCursor2 = miConexion2.cursor()

miCursor1.execute("SELECT PALABRA FROM PALABRAS")
palabras1 = miCursor1.fetchall()

miCursor2.execute("SELECT PALABRA FROM PALABRAS")
palabras2 = miCursor2.fetchall()

palabras1 = [palabra[0] for palabra in palabras1]
palabras2 = [palabra[0] for palabra in palabras2]

palabrasNoCoincidentes = []

for palabra1 in palabras1:
    if palabra1 not in palabras2:
        palabrasNoCoincidentes.append(palabra1)

for palabraNoCoincidente in palabrasNoCoincidentes:
    print(palabraNoCoincidente)

if palabrasNoCoincidentes == []:
    print("TODAS LAS PALABRAS DE LA BBDD1K ESTAN EN LA BBDD10K")

miConexion1.close()
miConexion2.close()
