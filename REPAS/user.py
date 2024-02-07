'''
Crear un arxiu de nom user.py. En aquest arxiu s’ha de crear una class de nom user. Aquesta class ha de tindre:
Constructor, Atributs (mínim 6), Getters/Setters
Mètode de nom salutacio on es mostren, per pantalla, totes les dades (atributs) del user.
Afegir el mètode to_dict(self) a les dues classes per retornar l’objecte en format json
'''
import json

class user:
    def __init__(self, nom, cognom, edat, email, telefon, dni):
        self.nom = nom
        self.cognom = cognom
        self.edat = edat
        self.email = email
        self.telefon = telefon
        self.dni = dni

    def getNom(self):
        return self.nom
    def setNom(self, nom):
        self.nom = nom

    def getCognom(self):
        return self.cognom
    def setCognom(self, cognom):
        self.cognom = cognom
    
    def getEdat(self):
        return self.edat
    def setEdat(self, edat):
        self.edat = edat
    
    def getEmail(self):
        return self.email
    def setEmail(self, email):
        self.email = email

    def getTelefon(self):
        return self.telefon
    def setTelefon(self, telefon):
        self.telefon = telefon

    def getDni(self):
        return self.dni
    def setDni(self, dni):
        self.dni = dni

    def salutacio(self):
        print(f'Benvingut/da! Aquestas són les teves dades: \n'
              f'Nom: {self.nom}\n'
              f'Cognom: {self.cognom}\n'
              f'Edat: {self.edat}\n'
              f'Email: {self.email}\n'
              f'Telèfon: {self.telefon}\n'
              f'DNI: {self.dni}')

    def to_dict(self):
        usuari = {
            "nom": self.getNom(),
            "cognom": self.getCognom(),
            "edat": self.getEdat(),
            "email": self.getEmail(),
            "telefon": self.getTelefon(),
            "dni": self.getDni()
        }
        return usuari
    
    def to_json(self):
        user_dict = self.to_dict()
        user_json = json.dumps(user_dict, indent=2)
        return user_json

usuari = user('Juan', 'Perez', 23, 'exemple@iticbcn.cat', '739146987', '01234567E')
usuari.salutacio()
# usuari json
print(usuari.to_json())