# Crear una funció que agafi una llista amb 10 números, i retorni una altra llista amb els seus quadrats.
def llistaQuadrat(nums):
    quadrat = [pow(n,2) for n in nums]
    return quadrat