'''Crear una funció que sumi dos números passats per paràmetre. Aquests números seran demanats a l’usuari. 
(En aquest cas haurieu de tindre un arxiu on feu el càlcul de dos números passats per paràmetre i un 
arxiu main.py on trucarà aquesta funció i li passarà els números indicats per l’usuari.)
'''
from exercici27 import suma

n1 = int(input('Introdueix un número: '))
n2 = int(input('Introdueix altre número: '))

print(f'{n1} + {n2} = {suma(n1, n2)}')