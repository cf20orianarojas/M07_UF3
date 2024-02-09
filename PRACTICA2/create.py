# funció que retorna la query que inserta dades en la BBDD
from connection import *

def create():

    insert = '''
                INSERT INTO tascas(nom_tasca, data_inici, data_fi, prioritat, estat) 
                VALUES ('Pràctica 2', '2024-02-08', '2024-02-11', true, 'Pendiente');
    '''
    connection.execute(insert)
    print(connection)
    conn.commit()

    # return insert

create()