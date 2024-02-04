'''Crear una funció que passats dos números per paràmetre (demanats a l’usuari) ens mostra per pantalla tots 
els números (enters) que hi ha entre ells. També mostrarà per pantalla la suma d’aquests números enters.'''
from exercici29 import intervalNum
n1 = int(input('Introdueix un número: '))
n2 = int(input('Introdueix altre número: '))

result = intervalNum(n1, n2)
print(result)