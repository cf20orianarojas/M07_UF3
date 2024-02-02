'''
Demanar a l’usuari posar 2 paraules. Afegir aquestes a una tupla i 
mostrar per pantalla quantes vegades apareix cada lletra.
'''
paraula = input('Posa 2 paraules: ')
tupla = tuple(paraula.replace(" ", ""))
lletres = set(tupla)

for l in lletres:
    print(f'{l}: {tupla.count(l)}')