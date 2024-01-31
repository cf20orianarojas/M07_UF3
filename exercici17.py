'''
Igual que l’anterior però a la tupla afegir la frase sense els caràcters repetits i mostrar el 
contingut de la tupla. Exemple: Usuari indica la paraula caracteristica. Es mostra per pantalla carteis.
'''
frase = input('Introdueix una frase: ')
tupla = tuple(sorted(set(frase), key=frase.index))
print(tupla)