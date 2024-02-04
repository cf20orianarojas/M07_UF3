'''
Crear un arxiu de nom vehicle.py. En aquest arxiu s’ha de crear una class de nom vehicle. 
Aquesta class ha de tindre: Constructor, Atributs (mínim 6), Getters/Setters
Mètode de nom parts on es mostren, per pantalla, totes les dades (atributs) del vehicle.
Afegir el mètode to_dict(self) a les dues classes per retornar l’objecte en format json
'''
class vehicle:
    # constructor de classe
    def __init__(self, marca, model, any, color, matricula, preu):
        self.marca = marca
        self.model = model
        self.any = any
        self.color = color
        self.matricula = matricula
        self.preu = preu
    
    # getters/setters de atributs
    def getMarca(self):
        return self.marca
    def setMarca(self, marca):
        self.marca = marca

    def getModel(self):
        return self.model
    def setModel(self, model):
        self.model = model

    def getAny(self):
        return self.any
    def setAny(self, any):
        self.any = any

    def getColor(self):
        return self.color
    def setColor(self, color):
        self.color = color

    def getMatricula(self):
        return self.matricula
    def setMatricula(self, matricula):
        self.matricula = matricula

    def getPreu(self):
        return self.preu
    def setPreu(self, preu):
        self.preu = preu

    def parts(self):
        print(f'Marca: {self.getMarca()}\n'
              f'Model: {self.getModel()}\n'
              f'Any: {self.getAny()}\n'
              f'Color: {self.getColor()}\n'
              f'Matricula: {self.getMatricula()}\n'
              f'Preu: {self.getPreu()} €')
        
    def to_dict(self):
        vehicle = {
            "marca": self.getMarca(), 
            "model": self.getModel(),
            "any": self.getAny(),
            "color": self.getColor(),
            "matricula": self.getMatricula(),
            "preu": self.getPreu()
        }
        return vehicle
    
coche = vehicle('Ford', 'F-150', 2023, 'Azul', '123ABC', 25000.000)
coche.parts()