# Funció crear taula
def crea_taula():
    # prioritat (t / f)
    query = '''CREATE TABLE IF NOT EXISTS tascas(
                    id_tasca SERIAL PRIMARY KEY,
                    nom_tasca VARCHAR(255) NOT NULL,
                    data_inici DATE NOT NULL DEFAULT CURRENT_DATE,
                    data_fi DATE NOT NULL DEFAULT CURRENT_DATE,
                    prioritat BOOLEAN NOT NULL,
                    estat VARCHAR(255) NOT NULL
    )''' 
    return query