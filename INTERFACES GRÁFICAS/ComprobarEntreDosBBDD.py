from sqlite3 import connect

miConexion1 = connect(r'C:/Users/MARTI/Desktop/PYTHON/BBDD/PALABRAS_WORDLE_1K')
miCursor1 = miConexion1.cursor()
miCursor1.execute("SELECT PALABRA FROM PALABRAS")

palabras1000 = set(miCursor1.fetchall())

miConexion2 = connect(r'C:/Users/MARTI/Desktop/PYTHON/BBDD/PALABRAS_WORDLE_10K')
miCursor2 = miConexion2.cursor()
miCursor2.execute("SELECT PALABRA FROM PALABRAS")

palabras10000 = set(miCursor2.fetchall())

palabras_faltantes = palabras1000 - palabras10000

if palabras_faltantes:
    print("Las siguientes palabras están en la base de datos 'PALABRAS_WORDLE_1K' pero no están en 'PALABRAS_WORDLE_10K':")
    for palabra in palabras_faltantes:
        print(palabra)
else:
    print("Todas las palabras de la base de datos 'PALABRAS_WORDLE_1K' están también en 'PALABRAS_WORDLE_10K'.")
    
miConexion1.close()
miConexion2.close()
