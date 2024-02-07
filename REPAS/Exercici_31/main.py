'''Crear una funció per calcular el total d’una factura amb l’IVA. La funció ha de rebre (per paràmetre) la 
quantitat sense IVA i l’IVA a aplicar (introduïts per l’usuari). En cas de no passar-li cap valor o un valor 
erroni (4%, 10% o 21%) s’aplicarà directament el 21%. Es mostra per pantalla el valor sense IVA, l’IVA i el total.'''
from exercici31 import aplicarIVA

valor = int(input('Introduce un valor en euros: '))
iva = int(input('Introduce el IVA a aplicar (4%, 10%, o 21%): '))

total = aplicarIVA(valor, iva)
print(f'Total amb l’IVA: {total}€')