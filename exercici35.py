'''Crear una funció que rebi una frase per paràmetre. Aquesta frase es demana a l’usuari. 
Ha de retornar un diccionari amb les paraules que conte i la longitud de cada paraula.'''
def dictFrase(frase):
    paraules = {}
    for i in frase.split(' '):
        paraules[i] = len(i)
    return paraules

frase = input('Introdueix una frase: ')
print(dictFrase(frase))