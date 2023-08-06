class Vehiculos():

    def __init__(self, marca, color):
        self.marca = marca
        self.color = color

        self.enMarcha = False
        self.acelera = False
        self.frena = False

    def arrancar(self):
        self.enMarcha = True

    def acelerar(self):
        self.acelera = True

    def frenar(self):
        self.frena = True

    def estado(self):
        print("\nMarca: ", self.marca, "\nColor: ", self.color, "\nEn marcha: ", self.enMarcha, "\nAcelerando: ", self.acelera, "\nFrenando: ", self.frena)


class VElectricos():
    def __init__(self):
        self.autonomia = 100

        def cargandoEnergia(self):
            self.cargando = True


class Furgoneta(Vehiculos):

    def carga(self, conCarga):
        self.conCarga = conCarga
        if(self.conCarga):
            print("La furgoneta lleva carga")
        else:
            print("La furgoneta no lleva carga")



class Moto(Vehiculos):
    haciendoCaballito = ""
    def caballito(self):
        self.haciendoCaballito = "La moto va haciendo el caballito"

    def estado(self):
        print("\nMarca: ", self.marca, "\nColor: ", self.color, "\nEn marcha: ", self.enMarcha, "\nAcelerando: ", self.acelera, "\nFrenando: ", self.frena, "\n", self.haciendoCaballito)
 
    
moto1 = Moto("Honda", "rojo")

moto1.caballito()

moto1.estado()

furgoneta1 = Furgoneta("Renault", "blanco")

furgoneta1.arrancar()

furgoneta1.estado()

furgoneta1.carga(True) 


class biciElectrica(Vehiculos, VElectricos):
    pass

bici1 = biciElectrica("HB", "verde")

bici1.arrancar()

bici1.acelerar()

bici1.estado()
