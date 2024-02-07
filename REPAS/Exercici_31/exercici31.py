'''Crear una funció per calcular el total d’una factura amb l’IVA. La funció ha de rebre (per paràmetre) la 
quantitat sense IVA i l’IVA a aplicar (introduïts per l’usuari). En cas de no passar-li cap valor o un valor 
erroni (4%, 10% o 21%) s’aplicarà directament el 21%. Es mostra per pantalla el valor sense IVA, l’IVA i el total.'''
def aplicarIVA(valor, iva):
    if iva not in [4, 10, 21]:
        print('L’IVA a aplicar no és vàlid només 4%, 10% i 21%, s’aplicarà el 21%\n')
        iva = 21
    tasa = iva / 100
    total = valor + (valor*tasa)
    return total