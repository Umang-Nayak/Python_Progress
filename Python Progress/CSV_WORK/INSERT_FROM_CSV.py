import csv
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

csv_file = "your_file.csv"


try:
    with open(csv_file, "r") as file:
        csv_reader = csv.reader(file)
        next(csv_reader)  # Skip the header row if it exists

        for row in csv_reader:
            # Assuming the CSV file columns match your database table's columns
            sql = "INSERT INTO student (s_id, s_name, s_std, s_div) VALUES (%s, %s, %s, %s)"
            mc.execute(sql, (row[0], row[1], row[2], row[3]))

    mydb.commit()
    mc.close()
    mydb.close()
    print("Data inserted successfully.")

except (Exception, psycopg2.Error) as error:
    print("Error inserting data:", error)

