#

def create():
    insert = '''
                INSERT INTO tascas(id_tasca, nom_tasca, data_inici, data_fi, prioritat, estat) 
                VALUES (1, 'Pràctica 2', '2024-02-08', '2024-02-11', true, 'Pendiente');
    '''
    return insert