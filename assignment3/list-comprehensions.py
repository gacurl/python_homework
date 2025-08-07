# Task 3: List Comprehensions Practice
import csv

with open ("../csv/employees.csv", newline='') as file:
    rows = []
    reader = csv.reader(file)

    for row in reader:
        rows.append(row)
    
    full_name = [row[1] + " " + row[2] for row in rows[1:]]
    print(full_name)

    names_with_e = [name for name in full_name if 'e' in name]
    print(f"Names with 'e':", names_with_e)