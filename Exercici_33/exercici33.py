'''Crear una funció que rebi un diccionari amb una llista de la compra (amb preus i descomptes).
Exemple llista compra: {100:10, 250:5, 1500:30, …} on 100 és el preu i 20 el descompte a aplicar a aquests 100.
Demanar a l’usuari l’IVA a aplicar al total de la llista de la compra.
Mostrar per pantalla els valors amb el descompte aplicat més l’IVA.
Exemple: cantitat con desc = cantitat - (cantitat*desc)
Producte 1: 
Producte 2: '''
def llistaCompra(llista):
    iva = int(input('Introduce el IVA a aplicar (4%, 10%, o 21%): '))
    if iva not in [4, 10, 21]:
        iva = 21
    llista_final = {}
    for producte, (preu, desc) in enumerate(llista.items(), start=1):
        descompte = preu - (preu * (desc/100))
        tasa = iva / 100
        desc_mes_iva = descompte + (descompte*tasa)

        llista_final[producte] = desc_mes_iva

        print(f'\nProducte {producte}\nPreu total amb IVA({iva}%): {desc_mes_iva}€')
    return llista_final

dict = {100:10, 250:5, 1500:30}
print(f'\nPreus final: {llistaCompra(dict)}')