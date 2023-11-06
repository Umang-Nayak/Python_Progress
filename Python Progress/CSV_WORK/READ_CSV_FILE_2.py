import csv

# Open the CSV file for reading
with open('your_file.csv', newline='') as csvfile:
    reader = csv.reader(csvfile)

    # Iterate through each row in the CSV file
    for row in reader:
        # Each row is a list of values
        print(row)


""" 
# Only for 1st column 

    for row in reader:
        first_value = row[0]
        print(first_value)
"""