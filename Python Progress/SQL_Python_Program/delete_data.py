import psycopg2

mydb = psycopg2.connect(
    host="localhost",
    user="postgres",
    password="kingun39",
    port=5432,
    database="UMA"
)
mc = mydb.cursor()

mc.execute("SELECT * FROM student")
# mc.execute("SELECT s_name FROM student")
myresult = mc.fetchall()
# myresult = mc.fetchone()

print("\nTABLE DATA BEFORE DELETE :- ")
for x in myresult:
    print(x)


d = int(input("\nEnter student ID for delete = "))
mc.execute(f"DELETE FROM student WHERE s_id = {d};")


mc.execute("SELECT * FROM student")
myresult = mc.fetchall()
print("\nTABLE DATA AFTER DELETE :- ")
for x in myresult:
    print(x)


mydb.commit()
mydb.close()
