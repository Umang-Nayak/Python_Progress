import psycopg2

mydb = psycopg2.connect(
    host="localhost",
    user="postgres",
    password="kingun39",
    port=5432,
    database="UMA"
)


mc = mydb.cursor()

mc.execute("SELECT * FROM teacher")
# mc.execute("SELECT s_name FROM student")

# myresult = mc.fetchall()
myresult = mc.fetchone()

for x in myresult:
    print(x)
