'''
Crear una funció que passats dos números per paràmetre (demanats a l’usuari) 
ens mostri per pantalla un número aleatori entre aquests dos números.
'''
import random

def randomNum(n1, n2):
    return random.randint(n1, n2)