from sqlite3 import *

miConexion = connect(r"C:\Users\MARTI\Desktop\PYTHON\BBDD\ShoeBase")

miCursor = miConexion.cursor()




# miCursor.execute("CREATE TABLE SHOES (ID INTEGER PRIMARY KEY AUTOINCREMENT, SKU VARCHAR(25) UNIQUE, MODELO VARCHAR(50), COLORWAY VARCHAR(50), MARCA VARCHAR(25), PRECIO INTEGER)")

# miCursor.execute("INSERT INTO SHOES VALUES(NULL, 'DN3707-100', 'JORDAN 3', 'WHITE CEMENT REIMAGINED', 'NIKE', 210)")

# viariasShoes = [("DZ5485-612", "JORDAN 1", "CHICAGO LOST & FOUND", "NIKE", 180), 
#                 ("DM0807-400", "DUNK SB", "RASPBERRY BLUE", "NIKE", 110),
#                 ("DM0108-002", "DUNK", "GRAFFITI PINK", "NIKE", 130),
#                 ("AQ9129-200", "JORDAN 4", "FOSSIL", "NIKE", 175)]

# miCursor.executemany("insert into SHOES values(NULL,?,?,?,?,?)", viariasShoes)




miCursor.execute("SELECT * FROM SHOES")

listaShoes = miCursor.fetchall()

for shoe in listaShoes:
    print("SKU:", shoe[1], "MODELO:", shoe[2], "COLORWAY:", shoe[3], "MARCA:", shoe[4], "PRECIO:", shoe[5])




miConexion.commit()

miConexion.close()