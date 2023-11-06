import psycopg2

mydb = psycopg2.connect(
    host="localhost",
    user="postgres",
    password="kingun39",
    port=5432,
    database="UMA"
)
mc = mydb.cursor()

sql = "INSERT INTO student(s_id, s_name, s_age, s_std, s_div) VALUES (%s, %s, %s, %s, %s);"

while True:
    choice = input("Add Data ? y/n = ")

    if choice == "y":
        sid = int(input("Enter ID = "))
        sname = input("Enter Name = ")
        sage = int(input("Enter Age = "))
        sstd = int(input("Enter Standard = "))
        sdiv = input("Enter Division = ")

        # Execute the INSERT statement for each set of values
        mc.execute(sql, (sid, sname, sage, sstd, sdiv))
        mydb.commit()

        print("Data Added to Student Table Successfully!")
    else:
        print("Data Entry Complete")
        break

mydb.close()
