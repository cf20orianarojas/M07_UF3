# Buscar error/s en el següent programa. Aquest programa elimina el contacte (nom i telèfon) segons el nom passat per paràmetre.
contactes = {'Roger':678232311, 'Oriol':566879326}

def elimina(contactes, user):
    if user in contactes:
        del contactes[user]
    return contactes

print(elimina(contactes, 'Pablo'))