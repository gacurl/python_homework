# Task 1: Hello
def hello():
    return "Hello!"
# Task 2: Greet with a Formatted String
def greet(name):
    return f"Hello, {name}!"
# Task 3: Calculator
def calc(x, y, operation='multiply'):
    try:
        if operation == 'add':
            return x + y
        elif operation == 'subtract':
            return x - y
        elif operation == 'multiply':
            return x * y
        elif operation == 'divide':
            return x / y
        elif operation == 'modulo':
            return x % y
        elif operation == 'int_divide':
            return x // y
        elif operation == 'power':
            return x ** y
    except ZeroDivisionError:
        return "You can't divide by 0!"
    except Exception:
        return "You can't multiply those values!"
    else:
        return "Operation not recognized."
# Task 4: Data Type Conversion
def data_type_conversion(value, name):
    if name == 'int':
        return int(value)
    elif name == 'float':
        return float(value)
    elif name == 'str':
        return str(value)
           