import psycopg2

mydb = psycopg2.connect(
    host="localhost",
    user="postgres",
    password="kingun39",
    port=5432,
    database="UMA"
)
cs = mydb.cursor()


def connect_database():
    try:
        if cs:
            print("\n<----- DATABASE CONNECTED SUCCESSFULLY ----->")
        else:
            print("\n !!! DATABASE NOT CONNECTED !!! ")

    except Exception as e:
        print("\n!!! ERROR !!!")
        print(f"Error type = {e}")

    print("--------------------------------------------------")


def create_table():
    try:
        table_name = input("\nEnter Table Name = ")
        column_name = input("Enter 1st Column Name = ")
        datatype = input(f"Enter Datatype of {column_name} = ")
        constrain = input(f"Enter Constrain for {column_name} = ")

        # Create Table
        cs.execute(f"CREATE TABLE {table_name}({column_name} {datatype} {constrain})")
        c = 2
        while True:
            choice = input(f"\nAdd Column Number {c} : y/n = ")
            if choice == "y":
                column_name = input("Enter Column Name = ")
                datatype = input(f"Enter Datatype of {column_name} = ")
                constrain = input(f"Enter Constrain of {column_name} = ")
                # Add Column
                cs.execute(f"ALTER TABLE {table_name} ADD {column_name} {datatype} {constrain}")
                c = c + 1

            else:
                print(f"\nYour {table_name} Table Created Successfully !!!")
                break
        mydb.commit()

    except Exception as e:
        print("\n!!! ERROR !!!")
        print(f"Error type = {e}")

    print("--------------------------------------------------")


def insert_data():
    try:
        sql = f"INSERT INTO student(s_id, s_name, s_age, s_std, s_div) VALUES (%s,%s,%s,%s,%s);"
        val = []

        while True:
            choice = input("\nAdd Data ? (y/n) = ")

            if choice == "y":
                sid = int(input("Enter ID = "))
                sname = input("Enter Name = ")
                sage = int(input("Enter Age = "))
                sstd = int(input("Enter Stander = "))
                sdiv = input("Enter Division = ")

                val.append((sid, sname, sage, sstd, sdiv))

                print("\nTable Data =")
                for i in range(len(val)):
                    print(f"{i+1} = {val[i]}")

            else:
                if val:
                    cs.executemany(sql, val)
                    mydb.commit()
                    print(f"\n{len(val)} records added to Student Table successfully.")
                else:
                    print("\nNo Data To Insert !!!")
                break

    except Exception as e:
        print("\n!!! ERROR !!!")
        print(f"Error type = {e}")

    print("--------------------------------------------------")


def update_data():
    try:
        cs.execute("SELECT * FROM student")
        myresult = cs.fetchall()

        print("\nTABLE DATA BEFORE UPDATE :- ")
        for x in myresult:
            print(x)

        cn = input("\nEnter column name you want to update = ")
        osi = input("Enter old data of given column for update = ")
        nsi = input("Enter updated data = ")

        sql = "UPDATE student SET {} = %s WHERE {} = %s".format(cn, cn)
        cs.execute(sql, (nsi, osi))

        cs.execute("SELECT * FROM student")
        myresult = cs.fetchall()
        print("\nTABLE DATA AFTER UPDATE :- ")
        for x in myresult:
            print(x)
        mydb.commit()

    except Exception as e:
        print("\n!!! ERROR !!!")
        print(f"Error type = {e}")

    print("--------------------------------------------------")


def select_data():
    try:
        print("\nWrite star(*) for all columns !!!")
        print("Or write a column name separated by comma(,) in single line !!!")

        table_name = input("\nEnter table name = ")
        column_name = input("Enter column name = ")

        cs.execute(f"SELECT {column_name} FROM {table_name}")
        myresult = cs.fetchall()

        print(f"\nData of {table_name} table :-")
        for x in myresult:
            print(x)

    except Exception as e:
        print("\n!!! ERROR !!!")
        print(f"Error type = {e}")

    print("--------------------------------------------------")


def delete_data():
    try:
        cs.execute("SELECT * FROM student")
        myresult = cs.fetchall()

        print("\nTABLE DATA BEFORE DELETE :- ")
        for x in myresult:
            print(x)

        d = int(input("\nEnter student ID for delete = "))
        cs.execute(f"DELETE FROM student WHERE s_id = {d};")

        cs.execute("SELECT * FROM student")
        myresult = cs.fetchall()
        print("\nTABLE DATA AFTER DELETE :- ")
        for x in myresult:
            print(x)
        mydb.commit()

    except Exception as e:
        print("\n!!! ERROR !!!")
        print(f"Error type = {e}")

    print("--------------------------------------------------")


while True:
    print("\nSELECT NUMBER FOR OPERATION :-")
    print("0. FOR EXIT PROGRAM")
    print("1. CHECK CONNECTION TO DATABASE")
    print("2. CREATE TABLE IN DATABASE")
    print("3. INSERT DATA IN TABLE")
    print("4. UPDATE DATA IN TABLE")
    print("5. DELETE DATA IN TABLE")
    print("6. READ DATA FROM TABLE")

    ch = int(input("\nEnter Choice = "))

    if ch == 1:
        connect_database()
    elif ch == 2:
        create_table()
    elif ch == 3:
        insert_data()
    elif ch == 4:
        update_data()
    elif ch == 5:
        delete_data()
    elif ch == 6:
        select_data()
    else:
        print("\nThank You.")
        print("Visit Again.")
        break

cs.close()
mydb.close()
