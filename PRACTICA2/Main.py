# Fitxer de gestió de totes les peticions del client
from connection import *
from create_table import crea_taula

try:
    # operacions de CRUD
    taula = crea_taula()

    # create =
    # read =
    # update =
    # delete =
    
    # execute envia la query corresponent (create, read, update, delete)
    connection.execute(query)

    # fa efectius els canvis de la query.
    conn.commit()

    print(connection)
except (Exception, psycopg2.Error) as error:
    print('Error', error)
finally:
    conn.close()