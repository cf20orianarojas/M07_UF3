'''
Demanar a l’usuari posar 2 paraules. Afegir aquestes a una tupla i 
mostrar per pantalla quantes vegades apareix cada lletra.
'''
paraula = input('Posa 2 paraules: ')
tupla = tuple(paraula.replace(' ',''))
count = {} # diccionari per comptar

for lletra in paraula:
    if lletra in count:
        count[lletra]+=1
    else:
        count[lletra]=1

for lletra, count in count.items():
    print(f'{lletra}: {count}')
print(tupla)