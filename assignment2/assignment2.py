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



