'''
Demanar a l’usuari que introdueixi 10 números separats per un espai. Al acabar, el programa els 
introduirà en una tupla i els ordenarà (major o menor, com volgueu), mostrant per pantalla el contingut de la tupla.
'''
n = input('Introdueix 10 números separats per un espai ')
tupla = ()

for x in n:
    if x != ' ':
        tupla+=(int(x),)

lista = list(tupla)
lista.sort()
tupla = tuple(lista)
print(tupla)