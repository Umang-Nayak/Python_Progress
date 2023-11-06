import psycopg2

mydb = psycopg2.connect(
    host="localhost",
    user="postgres",
    password="kingun39",
    port=5432,
    database="sigma"
)
mc = mydb.cursor()
if mc:
    print("----- DATABASE CONNECTED -----")
else:
    print(" !!! DATABASE NOT CONNECTED !!! ")


try:
    table_name = input("Enter Table Name = ")
    column_name = input("Enter 1st Column Name = ")
    datatype = input(f"Enter Datatype of {column_name} = ")
    constrain = input(f"Enter Constrain for {column_name} = ")

    # Create Table
    mc.execute(f"CREATE TABLE {table_name}({column_name} {datatype} {constrain})")
    c = 2
    while True:
        choice = input(f"\nAdd Column Number {c} : y/n = ")
        if choice == "y":
            column_name = input("Enter Column Name = ")
            datatype = input(f"Enter Datatype of {column_name} = ")
            # Add Column
            mc.execute(f"ALTER TABLE {table_name} ADD {column_name} {datatype}")
            c = c + 1

        else:
            print(f"\nYour Columns Added To {table_name} Table Successfully !!!")
            break


except Exception as e:
    print("\n!!! ERROR !!!")
    print(f"Error type = {e}")


mydb.commit()
