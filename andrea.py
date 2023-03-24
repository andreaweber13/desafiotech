#não consegui rodar o servidor localmente
import psycopg2

emissor = psycopg2.connect(
    host="localhost",
    database="dvdrental",
    user="postgres",
    password="password"
)
emissor_cursor = emissor.cursor()
emissor_cursor.execute("select * from nometabela")
colunas = emissor_cursor.fetchall()
receptor = psycopg2.connect(
    host="localhost",
    database="analytics",
    user="postgres",
    password="password"
)
receptor_cursor = receptor.cursor()
for coluna in colunas:
    receptor_cursor.execute("INSERT INTO NOMETABELA VALUES (%s, %s,  %s, %s)",coluna)


receptor_cursor.commit()

receptor_cursor.close()
receptor.close()
emissor_cursor.close()
emissor.close()
