# Task 4: Closure Practice
def make_hangman(secret_word):
    guesses = [] # if inside, it'll reset every time

    def hangman_closure(letter):
        guesses.append(letter)
        # for letter in secret_word: # loop through each letter in secret_word
        #     if letter not in guesses: # check if ALL letters in secret_word have been guessed (underscores remain)
        #         return False # return FALSE
        # build for loop with a list comprehension
        word_with_underscores = [letter if letter in guesses else "_" for letter in secret_word] # [expression for item in iterable if condition]
        print("".join(word_with_underscores)) # show progress

        # is the word guessed?
        if word_with_underscores == list(secret_word): # compare them
            print("You SOLVED it!") # winning message
            return True
        else:
            return False
    return hangman_closure

# mainline code
secret_word = input("What is the secret word? ")
play_game = make_hangman(secret_word)

while True:
    letter = input("Choose a letter: ")
    if play_game(letter):
        break