'''Crear una funció que passats dos números per paràmetre (demanats a l’usuari) ens mostra per pantalla tots 
els números (enters) que hi ha entre ells. També mostrarà per pantalla la suma d’aquests números enters.'''
def intervalNum(n1, n2):
    nums = 'Números: '
    suma = 0
    
    for i in range(n1, n2+1):
        nums+=f'{i}'
        suma+=i
    return f'{nums}\nSuma total: {suma}'