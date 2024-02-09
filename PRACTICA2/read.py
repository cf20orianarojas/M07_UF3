# funció read() que retorna query SELECT
from connection import *

def read_query():
    query = 'SELECT * FROM tascas;'
    
    connection.execute(query)
    row = connection.fetchone()
    print(row)
    conn.commit()
    #return query

read_query()