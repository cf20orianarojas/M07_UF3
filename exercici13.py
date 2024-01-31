'''
Demanar a l’usuari un número de l’1 al 10 i mostrar per pantalla la seva taula de multiplicar fins el 10. 
Exemple: l’usuari marca 3, es mostra per pantalla: 3,6,9,12,15,18,21,24,27 i 30
'''
n = int(input('Número entre 1 i 10 '))

for x in range(1, 11):
    print(f'{n} x {x} = {n*x}')