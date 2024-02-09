# Fitxer de gestió de totes les peticions del client
from connection import *
from create_table import crea_taula
from create import create_query
from read import read_query
from update import update_query
from delete import delete_query

try:
    operacion = input("¿Qué operación de CRUD quieres realizar? (T: Crear tabla, C: Crear Registro R: Leer, U: Actualizar, D: Eliminar): ").upper()

    # operacions de CRUD 
    operaciones = {
        'T': crea_taula(),
        'C': create_query(),
        'R': read_query(),
        'U': update_query(),
        'D': delete_query()
    }

    if operacion not in operaciones:
        print('Operación no válida')
    else:
        # La query sera la correspondiente a la operación seleccionada
        query = operaciones[operacion]

        print(query)
    
    # execute envia la query corresponent (table, create, read, update, delete)
    connection.execute(query)
    print(connection)

    # fa efectius els canvis de la query.
    conn.commit()
except (Exception, psycopg2.Error) as error:
    print('Error', error)
finally:
    connection.close()
    conn.close()