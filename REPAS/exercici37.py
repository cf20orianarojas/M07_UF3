# Buscar error/s en el següent programa:
ftotal = float(input('Introdueix el preu de tot el carrito: '))
def amb_iva(ftotal, iva = 21):
    ftotal = ftotal * (1+iva / 100) 
    return ftotal 
print(amb_iva(ftotal))