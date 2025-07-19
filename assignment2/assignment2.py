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