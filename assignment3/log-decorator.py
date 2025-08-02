# def show_inputs(*args, **kwargs):
#     print("Positional: ", args)
#     print("Keywords: ", kwargs)

# show_inputs(1, 2, 3, name="Alice", age=17)

# one time setup
import logging
logger = logging.getLogger(__name__ + "_parameter_log")
logger.setLevel(logging.INFO)
logger.addHandler(logging.FileHandler("./decorator.log","a"))
# ...
# # To write a log record:
# logger.log(logging.INFO, "this string would be logged")

def logger_decorator(func):
    def wrapper(*args, **kwargs):
        logger.info(f"function: {func.__name__}")
        logger.info(f"positional arguments: {args if args else 'none'}")
        logger.info(f"keyword arguments: {kwargs if kwargs else 'none'}")
        result = func(*args, **kwargs)
        logger.info(f"return {result}")
        return result
    return wrapper

# Step 3:
@logger_decorator
def hello_world():
    print("Hello World!")

hello_world()
# Step 4:
@logger_decorator
def pos_args(*args):
    return True

pos_args(3, "seventeen", 65)

# Step 5:
@logger_decorator
def keywrd_args(**kwargs):
    return logger_decorator

keywrd_args(name="Alice", age=30)
################################

