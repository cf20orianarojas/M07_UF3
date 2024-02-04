'''Crear una funció que rebi, per paràmetres, una funció i una llista. Ha de crear una llista 
nova amb el nou contingut i mostrar-la per pantalla.
Passes:
Crear una funció que calculi el quadrat d’un número passat per paràmetre.
Crear una segona funció que agafi cada número de la llista (passat per paràmetre) i 
truqui a la funció anterior i guardar el resultat a una llista.
'''
def num_quadrat(n):
    return pow(n, 2)

def llista_nums_quadrats(func, llista):
    llista_quadrat = [func(i) for i in llista]
    return llista_quadrat

llista = [i for i in range(1,11)]
resultat = llista_nums_quadrats(num_quadrat, llista)
print(f'Llista original: {llista}')
print(f'Llista al quadrat: {resultat}')