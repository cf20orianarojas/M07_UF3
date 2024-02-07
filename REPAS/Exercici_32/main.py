# Crear una funció que agafi una llista amb 10 números, i retorni una altra llista amb els seus quadrats.
from exercici32 import llistaQuadrat

llista = [int(i) for i in range(1, 11)]
resultat = llistaQuadrat(llista)
print(f'Llista original: {llista}\nLlista amb els seus quadrats: {resultat}')