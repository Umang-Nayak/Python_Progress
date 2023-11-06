import psycopg2
import csv

# Database connection parameters
db_params = {
    "host": "your_database_host",
    "database": "your_database_name",
    "user": "your_database_user",
    "password": "your_database_password",
}

# CSV file path
csv_file = "your_data.csv"

# Connect to the PostgreSQL database
try:
    connection = psycopg2.connect(**db_params)
    cursor = connection.cursor()

    # Open the CSV file
    with open(csv_file, "r") as file:
        csv_reader = csv.reader(file)
        next(csv_reader)  # Skip the header row if it exists

        for row in csv_reader:
            # Assuming the CSV file columns match your database table's columns
            query = "INSERT INTO your_table_name (column1, column2, column3) VALUES (%s, %s, %s)"
            cursor.execute(query, (row[0], row[1], row[2]))

    # Commit the changes and close the database connection
    connection.commit()
    cursor.close()
    connection.close()
    print("Data inserted successfully.")

except (Exception, psycopg2.Error) as error:
    print("Error inserting data:", error)
