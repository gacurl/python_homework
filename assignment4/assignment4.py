#%%
import pandas as pd

employee_dict = {
    'Name': ['Alice', 'Bob', 'Charlie'],
    'Age':  [25, 30, 35],
    'City': ['New York', 'Los Angeles', 'Chicago']
}
#print(employee_dict)

task1_data_frame = pd.DataFrame(employee_dict)
# print(task1_data_frame)
task1_with_salary = task1_data_frame.copy()
task1_with_salary['Salary'] = [70000, 80000, 90000]
# print (task1_with_salary)

task1_older = task1_with_salary.copy()
task1_older['Age'] += 1
# print(task1_older)

task1_older.to_csv('employees.csv', index=False)

# Task 2: Loading Data from CSV and JSON
task2_employees = pd.read_csv('employees.csv')
# print(task2_employees)

json_employees = pd.read_json('additional_employees.json')
# print(json_employees)

more_employees = pd.concat([task2_employees, json_employees], ignore_index=True)
# print(more_employees)

# Task 3: Data Inspection - Using Head, Tail, and Info Methods
first_three = more_employees.head(3)
print(first_three)

last_two = more_employees.tail(2)
print(last_two)


