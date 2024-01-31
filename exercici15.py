'''
El mateix que l’anterior exercici, però sense demanar un màxim de números. 
L’usuari indicarà quan ha acabat posant un 0.
'''
n = ''
tupla = ()
while n != '0':
    n = input('Introdueix números, el número 0 indicarà que has acabat: ')
    tupla+=(int(n),)

lista = list(tupla)
lista.sort()
tupla = tuple(lista)
print(tupla)