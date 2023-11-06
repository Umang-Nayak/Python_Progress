import psycopg2

mydb = psycopg2.connect(
    host="localhost",
    user="postgres",
    password="kingun39",
    port=5432,
    database="UMA"
)
mc = mydb.cursor()

# table_name = input("Enter Table Name = ")
# column_name = input("Enter Column Name = ")
sql = f"INSERT INTO student(s_id, s_name, s_age, s_std, s_div) VALUES (%s,%s,%s,%s,%s);"
val = []

while True:
    choice = input("Add Data ? (y/n) = ")

    if choice == "y":
        sid = int(input("Enter ID = "))
        sname = input("Enter Name = ")
        sage = int(input("Enter Age = "))
        sstd = int(input("Enter Stander = "))
        sdiv = input("Enter Division = ")

        val.append((sid, sname, sage, sstd, sdiv))
        print(f"Data ={val}")
    else:
        if val:
            mc.executemany(sql, val)
            mydb.commit()
            print(f"\n{len(val)} records added to Student Table successfully.")
        else:
            print("\nNo Data To Insert !!!")
        break


print(mc.rowcount, "record inserted.")
mydb.close()

"""
# 1
val=("John",)
mc.execute(sql, val)
mydb.commit()


# 2
val = [
    ('Peter',),
    ('Amy',)]
mc.executemany(sql, val)
mydb.commit()
"""
