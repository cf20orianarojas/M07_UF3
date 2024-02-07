'''
Crear una funció que passats dos números per paràmetre (demanats a l’usuari) 
ens mostri per pantalla un número aleatori entre aquests dos números.
'''
from exercici28 import randomNum
n1 = int(input('Introdueix un número: '))
n2 = int(input('Introdueix altre número: '))

result = randomNum(n1, n2)
print(result)