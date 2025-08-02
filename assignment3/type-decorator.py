# Task 2: A Decorator that Takes an Argument

def type_converter(type_of_output):
    def decorator(func):
        def wrapper(*args, **kwargs):
            # call the original function
            result = func(*args, **kwargs)
            # convert to desired type
            return type_of_output(result)
        return wrapper
    return decorator

# Step 3:
@type_converter(str)
def return_int():
    return 5

# Step 4:
@type_converter(int)
def return_string():
    return "not a number"

# Step 5:
y = return_int()
print(type(y).__name__) # This should print "str"

try:
   y = return_string()
   print("shouldn't get here!")
except ValueError:
   print("can't convert that string to an integer!") # This is what should happen