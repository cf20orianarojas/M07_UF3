# Funció que retorna la query per a eliminar dades de la BBDD
from connection import *

def delete_dades():
    query = 'DELETE FROM tascas;'
    
    connection.execute(query)
    conn.commit()
    print(connection)
    #return query