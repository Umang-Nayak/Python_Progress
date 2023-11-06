import psycopg2

mydb = psycopg2.connect(
    host="localhost",
    user="postgres",
    password="kingun39"
)

print(mydb)
