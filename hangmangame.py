import random

def get_word():
    words = ['python', 'hangman', 'developer', 'software', 'programming']
    return random.choice(words).lower()

def display_word(word, guessed_letters):
    display = ''
    for letter in word:
        if letter in guessed_letters:
            display += letter
        else:
            display += '_'
    return display

def hangman():
    word = get_word()
    guessed_letters = []
    tries = 6
    guessed = False

    print("Welcome to Hangman!")
    print(display_word(word, guessed_letters))
    print(f"You have {tries} tries remaining.")

    while not guessed and tries > 0:
        guess = input("Please guess a letter or the word: ").lower()

        if len(guess) == 1 and guess.isalpha():
            if guess in guessed_letters:
                print(f"You already guessed the letter '{guess}'.")
            elif guess not in word:
                print(f"'{guess}' is not in the word.")
                tries -= 1
                guessed_letters.append(guess)
            else:
                print(f"Good job! '{guess}' is in the word.")
                guessed_letters.append(guess)
                if all(letter in guessed_letters for letter in word):
                    guessed = True
        elif len(guess) == len(word) and guess.isalpha():
            if guess == word:
                guessed = True
            else:
                print(f"'{guess}' is not the correct word.")
                tries -= 1
        else:
            print("Invalid guess.")

        print(display_word(word, guessed_letters))
        print(f"You have {tries} tries remaining.")

    if guessed:
        print(f"Congratulations! You guessed the word '{word}'!")
    else:
        print(f"Sorry, you ran out of tries. The word was '{word}'.")

hangman()
