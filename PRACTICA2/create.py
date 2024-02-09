# funció que retorna la query que inserta dades en la BBDD
def create_query():
    insert = '''
                INSERT INTO tascas(nom_tasca, data_inici, data_fi, prioritat, estat) 
                VALUES ('Pràctica 2', '2024-02-08', '2024-02-11', true, 'Pendiente');
    '''
    
    return insert