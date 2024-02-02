'''
Demanar a l’usuari que posi 10 números separats per espais. Afegir aquests números a una llista. 
Calcular la suma de tots els números i la seva mitjana i afegir aquests 2 números a la llista. 
Mostrar per pantalla la llista.

Exemple mostra per pantalla.
Números de l’usuari:
suma total:
mitjana:
'''
x = input('Introdueix 10 números separats per un espai ')
num = x.split(' ')
num = [int(i) for i in num]
suma = 0

for n in num:
    suma+=n

mitja = int(suma/len(num))
num.extend([suma, mitja])

print(f'Suma total: {suma}')
print(f'Números de l’usuari: {x}')
print(f'Mitjana: {mitja}')
print(f'Llista: {num}')