from io import open

archivoExterno_texto = open("archivoExternoTexto.txt", "r+") #lectura y escritura



archivoExterno_texto.write("Prueba del seek (línea 1)")

archivoExterno_texto.write("\nEsto sería la segunda línea")
archivoExterno_texto.write("\nEsto sería la tercera línea")
archivoExterno_texto.write("\n4")
archivoExterno_texto.write("\n5")

archivoExterno_texto.seek(0) #llevar el puntero (cursor) a la posición 0 para poder leer el texto desde el principio


print(archivoExterno_texto.read())


archivoExterno_texto.close()



