# funció que retorna la query per a actualitzar les dades
from connection import *

def update_query():
    query = '''UPDATE tascas SET nom_tasca = 'UF3 Práctica 2', data_fi = '2024-01-09', estat = 'Acabada';'''
    
    connection.execute(query)
    conn.commit()
    print(connection)
    
    # return query