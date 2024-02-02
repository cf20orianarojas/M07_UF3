'''
Cal buscar la informació que es demana de la següent list:
areas_pis = [“Menjador”, 10.15, “Rebedor”, 9.56, “Habitació1”, 12.34, “Terrassa”, 15.55, “Lavabo”, 7.98, “Cuina”, 12, “Habitació2”, 12.23]
(Cal utilitzar els “:” per a que siguin vàlids els prints següents)
Imprimir el segon element
Imprimir l’últim element
Imprimir l’àrea de la terrassa
Imprimir del primer element al tercer element
Imprimir del tercer element a l’últim
Imprimir el total de l'àrea de les dues habitacions
Modificar l’àrea del lavabo i imprimir la nova list area
Afegir l'àrea de “pati interior” i 2.78 a les últimes posicions. Imprimir la nova list area.
Imprimir el total de l’àrea del pis.
'''
areas_pis = ['Menjador', 10.15, 'Rebedor', 9.56, 'Habitació1', 12.34, 'Terrassa', 15.55, 'Lavabo', 7.98, 'Cuina', 12, 'Habitació2', 12.23]
print(f'Segon element: {areas_pis[1]}')
print(f'Últim element: {areas_pis[-1]}')
print(f'Àrea de la terrasa: {[areas_pis.index('Terrassa')]}')
print(f'Des de el primer al tercer element: {areas_pis[0:3]}')
print(f'Des de el tercer element a l’últim: {areas_pis[2:]}')
print(f'Àrea total habitabions: {areas_pis[5] + areas_pis[-1]}')
areas_pis[9] = 8.50
print(f'Àrea del lavabo modificada: {areas_pis[9]}')
areas_pis.append("Pati interior")
areas_pis.append(2.78)
print(f'Nova llista: {areas_pis}')
total = areas_pis[1] + areas_pis[3] + areas_pis[5] + areas_pis[7] + areas_pis[9] + areas_pis[11] + areas_pis[13]
print(f'Àrea total del pis: {total}')