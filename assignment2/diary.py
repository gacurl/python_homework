# Task 1: Diary
# file writing, user input, error handling
import traceback

try:
    with open("diary.txt", "a") as file: # opens file for appending
        init_note_prompt = input("What happened today? ") # initial question
        file.write(init_note_prompt + "\n")
        # more notes you say?
        while True:
            # keep adding until break at "done for now"
            next_note_prompt = input("What else? ")

            if next_note_prompt == "done for now":
                file.write(next_note_prompt + "\n")
                break

            file.write(next_note_prompt + "\n")

except Exception as e: # catch any kind of error and name it e
    trace_back = traceback.extract_tb(e.__traceback__)
    stack_trace = list()
    for trace in trace_back: # format each traceback line
        stack_trace.append(f'File : {trace[0]} , Line : {trace[1]}, Func.Name : {trace[2]}, Message : {trace[3]}')
    print(f"Exception type: {type(e).__name__}")
    message = str(e)
    if message:
        print(f"Exception message: {message}")
    print(f"Stack trace: {stack_trace}") # print out where the error happened