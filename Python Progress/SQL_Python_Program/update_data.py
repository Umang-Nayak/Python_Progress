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

print("\nTABLE DATA BEFORE UPDATE :- ")
for x in myresult:
    print(x)

cn = input("\nEnter column name you want to update = ")
osi = input("Enter old data of given column for update = ")
nsi = input("Enter updated data = ")

# ERROR
# mc.execute(f"UPDATE student SET {cn} = {nsi} WHERE {cn} = {osi}")

sql = "UPDATE student SET {} = %s WHERE {} = %s".format(cn, cn)
mc.execute(sql, (nsi, osi))

mc.execute("SELECT * FROM student")
myresult = mc.fetchall()
print("\nTABLE DATA AFTER UPDATE :- ")
for x in myresult:
    print(x)


mydb.commit()
mydb.close()
