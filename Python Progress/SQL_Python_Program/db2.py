import psycopg2

mydb = psycopg2.connect(
    host="localhost",
    user="postgres",
    password="kingun39",
    port=5432
)

mycursor = mydb.cursor()
db = input("ENTER NAME OF DATABASE = ")
mycursor.execute(f"CREATE DATABASE {db}")
mycursor.execute("SHOW DATABASES")


print("Name of all database :-")
for x in mycursor:
    print(x)

mycursor.close()
mydb.close()
