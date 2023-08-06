import pickle

class Persona:
    def __init__(self, nombre, genero, edad):
        self.nombre = nombre
        self.genero = genero
        self.edad = edad
        print("Se ha creado una persona nueva con el nombre de", self.nombre)

    def __str__(self):
        return "{} {} {}".format(self.nombre, self.genero, self.edad)
    

class ListaPersonas:

    personas = []

    def __init__(self):
        listaDePersonas = open("ficheroExternoPersonas", "ab+")
        listaDePersonas.seek(0)

        try: #para que no de error si el fichero esta vacío
            self.personas = pickle.load(listaDePersonas)
            print("Se cargaron {} personas del fichero externo".format(len(self.personas)))
        except:
            print("El fichero esta vacío")
        finally:
            listaDePersonas.close()
            del(listaDePersonas)

    def agregarPersonas(self, p):
        self.personas.append(p)
        self.guardarPersonasEnFicheroExterno()

    def mostrerPersonas(self):
        for p in self.personas:
            print(p)

    def guardarPersonasEnFicheroExterno(self):
        listaDePersonas=open("ficheroExternoPersonas", "wb")
        pickle.dump(self.personas, listaDePersonas)
        listaDePersonas.close()
        del(listaDePersonas)

    def mostrarInfoFicheroExterno(self):
        print("La información del fichero externo es la siguiente:")
        for p in self.personas:
            print(p)

miLista = ListaPersonas()

persona = Persona("Antonio", "Masculino", 31)
miLista.agregarPersonas(persona)

miLista.mostrarInfoFicheroExterno()