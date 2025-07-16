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
def data_type_conversion(name, value):
    try:
        if value == 'int':
            return int(name)
        elif value == 'float':
            return float(name)
        elif value == 'str':
            return str(name)
    except ValueError:
        return f"You can't convert {name} into a {value}."

# Task 5: Grading System, Using *args
def grade(*args):
    try:
        average = sum(args) / len(args)
        if average >= 90:
            return 'A'
        elif average >= 80:
            return 'B'
        elif average >= 70:
            return 'C'
        elif average >= 60:
            return 'D'
        else:
            return 'F'
    except:
        return "Invalid data was provided."

# Task 6: Use a For Loop with a Range
def repeat(string, count):
    result = ""
    for j in range(count):
        result += string
    return result

# Task 7: Student Scores, Using **kwargs
def student_scores(choice, **kwargs):
    try:
        if choice == 'mean':
            return sum(kwargs.values()) / len(kwargs)
        elif choice == 'best':
            for name, score in kwargs.items():
                if score == max(kwargs.values()):
                    return name
    except:
        return "Please provide usable data."

# Task 8: Titleize, with String and List Operations
def titleize(phrase):
    try:
        little_words = ["a", "on", "an", "the", "of", "and", "is", "in"]
        words = phrase.split()
        result = []
        # title engineering starts here
        for i, word in enumerate(words):
            if i == 0 or i == len(words) - 1:
                # Capitalize the first and last word
                result.append(word.capitalize())
            elif word in little_words:
                # Keep little words lowercase
                result.append(word.lower())
            else:
                # Capitalize other words
                result.append(word.capitalize())
        return " ".join(result)
    except:
        return "Please provide a valid string."

# Task 9: Hangman, with more String Operations
def hangman(secret, guess):
    try:
        result = ""
        for letter in secret:
            if letter in guess:
                result += letter
            else:
                result += "_"
        return result
    except:
        return "Please provide valid strings."

# Task 10: Pig Latin, Another String Manipulation Exercise
def pig_latin(phrase):
    try:
        vowels = "aeiou"
        result = []
        words = phrase.split()
        # pig latin engineering starts here
        for word in words:
            if word.startswith("qu"):
                # move "qu " to the end
                pig = word[2:] + "quay"
            elif word[0] in vowels:
                # if word starts with a vowel, add "ay" to the end
                pig = word + "ay"
            else:
                # added after failing test of "qu"
                if "qu" in word:
                    i = word.index("qu") + 2 # handles "qu" chunk
                    pig = word[i:] + word[:i] + "ay"
                else:
                # move the first consonant cluster to the end and add "ay"
                    for i, char in enumerate(word):
                        if char in vowels:
                            pig = word[i:] + word[:i] + "ay"
                            break # stop the loop when the first vowel is found
            result.append(pig) # words to result
        
        return " ".join(result) # put it all together
    except:
        return "Please provide a valid string."