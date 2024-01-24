# Demanar a l’usuari que introdueixi 2 valors i mostrar, per pantalla, quin és el més gran.

x = input('Introdueix un valor numeric: ')
y = input('Introdueix altre valor numeric: ')

if int(x) < int(y):
    print(f'{int(y)} és més gran que {int(x)}')
elif int(x) > int(y):
    print(f'{int(x)} és més gran que {int(y)}')
else:
    print('Són iguals')