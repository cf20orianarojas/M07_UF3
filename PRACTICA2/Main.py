# Fitxer de gestió de totes les peticions del client
from connection import *
from create_table import crea_taula
from create import create_query
from read import read_query
from update import update_query
from delete import delete_query


try:
    operacion = input("¿Qué operación CRUD quieres realizar? (T: Crear tabla, C: Crear Registro R: Leer, U: Actualizar, D: Eliminar): ").upper()

    # operacions de CRUD
    options = ['T','C','R','U','D']


    # table = crea_taula()
    # create = create_query()
    # read = read_query()
    # update = update_query()
    # delete = delete_query()
    
    # execute envia la query corresponent (table, create, read, update, delete)
    
    connection.execute(query)

    # fa efectius els canvis de la query.
    conn.commit()
except (Exception, psycopg2.Error) as error:
    print('Error', error)
finally:
    conn.close()