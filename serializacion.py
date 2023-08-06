import pickle

#lista_nombres = ["Pepe", "Jose", "Ana", "Sara"]

#fichero_binario = open("lista_nombres", "wb") #escritura binaria

#pickle.dump(lista_nombres, fichero_binario)

#fichero_binario.close()

fichero = open("lista_nombres", "rb") #lectura binaria

lista = pickle.load(fichero)

print(lista)