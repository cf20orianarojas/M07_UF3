'''
Demanar a l’usuari un nùmero entre 10 i 100. Posar els números a una tupla desde 1 fins al número indicat per l’usuari. 
Exemple: usuari indica 34, es crea una tupla i es mostra per pantalla els números de l’1 al 34 (imprimint la tupla).
'''
n = int(input('Introdueix un número entre 10 i 100: '))
x = 1
tupla = ()
while x <= n:
    tupla += (x,)
    x+=1
print(tupla)