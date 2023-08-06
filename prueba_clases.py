class Vehiculos():

    def __init__(self, marca, color):
        self.marca = marca
        self.color= color

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


coche1 = Vehiculos("Seat", "rojo")
coche1.arrancar()
coche1.acelerar()

coche2 = Vehiculos("Toyota", "blanco")
coche2.arrancar()
coche2.frenar()

coche3 = Vehiculos("Subaru", "azul")

coche1.esado()
coche2.estado()
coche3.estado()



