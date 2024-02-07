# Fitxer de gestió de totes les peticions del client
from connection import *

try:

    # operacions de CRUD
    print(connection)
except (Exception, psycopg2.Error) as error:
    print('Error', error)
finally:
    conn.close()