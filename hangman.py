import random

# Initialized Variables
attempts = 6
dict_of_words = ["Apple","Banana", "Adventure", "Galaxy", "Pizza", 
                 "Volcano", "Cheetah", "Mystery", "Lantern", "Oxygen",
                 "Universe", "Dinosaur", "Robot", "Pirate", "Diamond",
                 "Castle", "Thunder", "Rainbow", "Coral", "Compass"
                 "Blizzard", "Chest", "Collect", "Paper", "Write"]
word_chosen = random.choice(dict_of_words).upper()
word_chosen_length = len(word_chosen)
list_of_letters_in_word = list(word_chosen)

# Hangman game.
def hangman():
    global attempts
    global list_of_letters_in_word
    global list_of_dash
    if letter_guessed in list_of_letters_in_word:
        indexes = [i for i, letter in enumerate(list_of_letters_in_word) if letter == letter_guessed]
        for i in indexes:
            list_of_dash[i] = list_of_letters_in_word[i]
        print(" ".join(list_of_dash))
        print(f"Correct. You have {attempts} attempts left.")
    elif letter_guessed not in list_of_letters_in_word:
        attempts -= 1
        print(f"Wrong guess. You have {attempts} attempts left. ")

# Dashes displayed indicates how many letters there are in the word.
list_of_dash = []
for i in range(word_chosen_length):
    list_of_dash.append("_")
print(" ".join(list_of_dash))

# Game running.
while "_" in list_of_dash and attempts > 0:
    letter_guessed = input("Guess a letter: ").upper()
    if len(letter_guessed) == 1:
        hangman()
    else:
        print("Enter one letter at a time!")
        quit()

# Ending of the game.
if attempts > 0:
    print("YOU WIN!")
elif attempts == 0:
    print("You lose :(")
    print(f"The word is {word_chosen}.")

print("Input:")
try:
    user_input = int(input("Enter a number to find all primes up to that number: "))
except:
    print("Only numbers!")
if user_input < 2:
    print("Try higher numbers.")
    quit()
elif user_input == 2:
    print("2")
elif user_input > 2:
    print("2")
    print("3")
    for i in range(2, user_input+1):
        prime = True
        for j in range(2, int(user_input ** 0.5)+1): # Take the square root of the input number to limit the number of factors.
            if i % j == 0:
                prime = False
                break
        if prime:
            print(i)
