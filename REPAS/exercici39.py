'''En el següent codi es vol demanar a l’usuari un número enter 
i mostri un triangle rectangle segons el número aportat per l’usuari.'''
n = int(input("Introdueix l’alçada del triangle (enter positiu): "))
for i in range(1, 2*n, 2):
    for j in range(i, 0, -2):
        print(j, end=" ")
    print("")