# paquet psycopg2
import psycopg2

# connexió de BD postgresql amb Python
conn = psycopg2.connect(
    database='postgres',
    user='practica2',
    password='admin',
    host='localhost',
    port='5432'
)

# comprovar la connexió amb mètode cursor()
connection = conn.cursor()
# print(connection)

# output en consola: <cursor object at 0x000002B17AF79C40; closed: 0>