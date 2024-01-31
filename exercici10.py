'''
Crear un arxiu on caldrà endevinar el número escollit pel programa entre 1 i 100. Cada vegada que l’usuari hi posi 
un número, caldrà indicar si és més petit o més gran fins que encerti i el missatge haurà d’indicar que ha encertat. 
Indicar també el número d’intents.
'''
import random

n = random.randint(1, 100)
# print(n)

x = int(input('Endevina el número (1 al 100) '))

while x != n:
    if x < n:
        print(f'El número és més gran que {x}')
    elif x > n:
        print(f'El número és més petit que {x}')
    x = int(input('Torna a intentar-ho '))

print(f'Has encertat! Él número era {x}')