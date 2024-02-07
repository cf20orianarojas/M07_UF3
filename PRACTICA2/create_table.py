# paquet psycopg2
import psycopg2
from connection import *

def crea_taula():
    # prioritat (t / f)
    # estado (estado actual de la tarea, como "pendiente", "en progreso" o "completa")
    query = '''CREATE TABLE IF NOT EXISTS tascas(
                    id_tasca SERIAL PRIMARY KEY,
                    nom_tasca VARCHAR(255) NOT NULL,
                    data_inici DATE NOT NULL DEFAULT CURRENT_DATE,
                    data_fi DATE NOT NULL DEFAULT CURRENT_DATE,
                    prioritat BOOLEAN NOT NULL,
                    estat VARCHAR(255) NOT NULL
    )''' 

    # execute envia la query
    connection.execute(query)
    # fa efectius els canvis de la query.
    conn.commit()