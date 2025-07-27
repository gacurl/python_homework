from datetime import datetime

# Task 2: Read a CSV File
import csv
import traceback

def read_employees():
    data_dict = {}  # store keys and values
    rows = []       # store rows

    try:
        with open("../csv/employees.csv", newline='') as file:
            reader = csv.reader(file)
            
            is_first = True
            for row in reader:
                if is_first:
                    data_dict["fields"] = row       # store the first row in the dict using the key "fields"
                    is_first  = False               # turn off the first row logic
                else:
                    rows.append(row)                # all other rows
            
            data_dict["rows"] = rows                # store all rows in dict

    except Exception as e:
        trace_back = traceback.extract_tb(e.__traceback__)
        stack_trace = list()
        for trace in trace_back:
            stack_trace.append(f'File : {trace[0]} , Line : {trace[1]}, Func.Name : {trace[2]}, Message : {trace[3]}')
        print(f"Exception type: {type(e).__name__}")
        message = str(e)
        if message:
            print(f"Exception message: {message}")
        print(f"Stack trace: {stack_trace}")

    return data_dict # return the dictionary

employees = read_employees()
print(employees)

# Task 3: Find the Column Index
def column_index(column_name):
    # Look for position of column_name
    return employees["fields"].index(column_name)

employee_id_column = column_index("employee_id")

# Task 4: Find the Employee First Name
def first_name(row_number): # a cell number - need column and row
    # use column index to find column number for "first_name"
    first_name_column_index = column_index("first_name")
    # get the row at the given row_number parameter
    first_name_row = employees["rows"][row_number]
    # Return that first name
    return first_name_row[first_name_column_index]  # extract just the first name

# Task 5: Find the Employee: a Function in a Function
def employee_find(employee_id):
    # define employee_match(row):
    def employee_match(row): # helper to filter rows
        return int(row[employee_id_column]) == employee_id # checks if this row is the one (True if matches - note the type conversion)
    # use filter to apply employee_match to employees["rows"]
    matches = list(filter(employee_match, employees["rows"])) # returns only rows that match the given ID and convert result to list
    return matches

# Task 6: Find the Employee with a Lambda
def employee_find_2(employee_id):
    matches = list(filter(lambda row: int(row[employee_id_column]) == employee_id , employees["rows"])) # lambda = for each row do X
    return matches

# Task 7: Sort the Rows by last_name Using a Lambda
def sort_by_last_name():
    last_name_index = column_index("last_name") # Find the column index of "last_name"
    # Sort the list of employee rows based on the last_name column
    employees["rows"].sort(key=lambda row: row[last_name_index]) # use a lambda + sort() method to extract the correct column; sorts IN PLACE
    # Return the sorted list of rows
    return employees["rows"]

# Task 8: Create a dict for an Employee
def employee_dict(row):
    employee_result_dict = {} # Initialize empty dict to store employee data

    for i in range(len(employees["fields"])): # loop through each column header index
        field = employees["fields"][i] # column name
        if field == "employee_id": #skip employee_id column
            continue
        employee_result_dict[field] = row[i]
    return employee_result_dict # Return the resulting dictionary

print("Task 8:")
print(employee_dict(employees["rows"][17]))

# Task 9: A dict of dicts, for All Employees
def all_employees_dict():
    employees_result_dict = {} # Initialize empty dict to hold the employee_id as keys

    for row in employees["rows"]:
        employee_id = row[employee_id_column]   # get employee_id from the row
        employee_details = employee_dict(row)   # call employee_dict() to get employee details
        employees_result_dict[employee_id] = employee_details # Add employee_id and employee dict to the new dict
    # Return the dictionary of employee dicts
    return employees_result_dict

all_employees = all_employees_dict()
print("Task 9:")
print(all_employees)

# Task 10: Use the os Module
import os

def get_this_value():
    return os.getenv("THISVALUE")

# Task 11: Creating Your Own Module
import custom_module

def set_that_secret(new_secret):
    custom_module.set_secret(new_secret)

set_that_secret("GUMBALL")

print("Task 11:")
print(custom_module.secret)

# Task 12: Read minutes1.csv and minutes2.csv

def read_minutes_file(file_path): # helper function that reads and returns dict
    result  = {}
    rows    = []

    try:
        with open(file_path, "r", newline="") as file: # open the file
            reader = csv.reader(file)

            headers = next(reader) # grab the first line
            result["fields"] = headers

            # get the rest
            for row in reader:
                rows.append(tuple(row)) # convert to a tuple
            result["rows"] = rows
    
    except Exception as err: # if something breaks, catch the error (err)
        trace_back = traceback.extract_tb(err.__traceback__)
        stack_trace = list()
        for trace in trace_back:
            stack_trace.append(f'File : {trace[0]} , Line : {trace[1]}, Func.Name : {trace[2]}, Message : {trace[3]}')
        print(f"Exception type: {type(err).__name__}")
        message = str(err)
   
        if message:
            print(f"Exception message: {message}")
        print(f"Stack trace: {stack_trace}")

    return result # return dict with headers and rows

def read_minutes(): # reads and returns from both files
    minutes1 = read_minutes_file("../csv/minutes1.csv")
    minutes2 = read_minutes_file("../csv/minutes2.csv")
    return minutes1, minutes2

minutes1, minutes2 = read_minutes() # store in global variable

# test and verify
print("Task 12: ")
print(minutes1)
print(minutes2)

# Task 13: Create minutes_set
def create_minutes_set():
    # convert rows to sets
    minutes_1_set = set(minutes1["rows"])
    minutes_2_set = set(minutes2["rows"])

    # Use the union operator (|) to combine both sets into one
    combined_minutes = minutes_1_set | minutes_2_set

    return combined_minutes # gather 'em up

minutes_set = create_minutes_set() # store in global variable

# Task 14: Convert to datetime
# from line is at top of file
def create_minutes_list():
    minutes_list = list(minutes_set) # convert set to list

    # convert 'em
    converted_list = list(
        map(
            lambda x: (x[0], datetime.strptime(x[1], "%B %d, %Y")),
            minutes_list
        )
    )

    return converted_list # return list with datetime objects

minutes_list = create_minutes_list() # store in global variable

print("Minutes with datetime objects:", minutes_list) # print to see conversion

# Task 15: Write Out Sorted List
def write_sorted_list():
    minutes_list.sort(key=lambda row: row[1]) # sort the list

    # Convert datetime objects using map
    converted = list(
        map(
            lambda row: (row[0], row[1].strftime("%B %d, %Y")),
            minutes_list
        )
    )

    # Write to minutes.csv
    with open("minutes.csv", "w", newline="") as file:
        writer = csv.writer(file)

        writer.writerow(minutes1["fields"]) # column headers

        for row in converted: # write rows
            writer.writerow(row)

    # Return the converted list
    return converted

minutes_written = write_sorted_list()
print(minutes_written)
