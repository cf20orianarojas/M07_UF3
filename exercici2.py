'''
Demanar a l’usuari que introdueixi un valor en €, seguidament demanar que introdueixi el IVA a aplicar-hi 
(4%, 10% o 21%) i finalment mostrar, per pantalla, el resultat del valor indicat per l’usuari, el % d’IVA 
demanat per l’usuari i el valor final amb l’IVA afegit. f = Precio con IVA=Precio sin IVA+(Precio sin IVA×Tasa de IVA)
'''
value = input('Introduce un valor en euros: ')
iva = input('Introduce el IVA a aplicar (4%, 10%, o 21%): ')

v = int(value)
tasa = int(iva) / 100

total = v + (v * tasa)

print(f'Valor: {v}€')
print(f'IVA: {int(iva)}%')
print(f'Valor amb l’IVA afegit: {total}€')