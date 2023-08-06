from sqlite3 import *

miConexion = connect(r"C:\Users\MARTI\Desktop\PYTHON\BBDD\WORDS_WORDLE_1K")

miCursor = miConexion.cursor()







# miCursor.execute("CREATE TABLE IF NOT EXISTS ESTADISTICAS (ID INTEGER PRIMARY KEY AUTOINCREMENT, WINS INTEGER, DEFEATS INTEGER)")
# miCursor.execute("INSERT INTO ESTADISTICAS VALUES(NULL, 0, 0)")

miConexion.commit()

miConexion.close()