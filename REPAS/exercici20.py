'''
Crear un diccionari on la clau (key) sigui un nom i el valor (value) l’edat. S’haura de demanar a 
l’usuari que posi contactes (noms i edats). Si algun nom es repeteix no s’fageirà al diccionari 
(indicant-ho a l’usuari). Es deixarà d’inserir contactes quan l’usuari indiqui que no vol afegir-ne més.
'''
n = input('Benvingut al diccionari! Enter per començar a afegir [ENTER]')
miDict = {}

while True:
    nom = input('Introdueix un nom: ')
    if nom in miDict:
        print('Aquest nom ja existeix dins del diccionari')
        continue
    edat = int(input('Introdueix l’edat: '))
    miDict[nom] = edat

    continuar = input('Vols afegir més contactes? (si/no)')
    if continuar == 'no':
        break
print(miDict)