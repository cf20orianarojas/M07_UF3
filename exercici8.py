'''
Demanar a l’usuari que posi entre 1 i 3 paraules. Al executar el programa, mostrarà la/es paraula/es 
indicada/es per l’usuari, indicar quants caràcters té i indicar el primer, i l’últim caràcter.
'''
p = input('Introdueix 3 paraules o una frase: ')

print(f'Paraules: {p}\nCaràcters totals: {len(p)}\nPrimer caràcter: {p[0]}\nÚltim caràcter: {p[len(p)-1]}')