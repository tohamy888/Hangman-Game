# Hangman Game

# Design a text-based Hangman game. The program
# selects a random word, and the player guesses one
# letter at a time to uncover the word. You can set a
# limit on the number of incorrect guesses allowed.


import random

def choose_word():
    # List of words to choose from
    words = ["apple", "banana", "orange", "grape", "pear"]
    return random.choice(words)

def display_word(word, guessed_letters):
    # Display the word with underscores for letters not guessed yet
    display = ""
    for letter in word:
        if letter in guessed_letters:
            display += letter
        else:
            display += "_"
    return display

def hangman():
    print("Welcome to Hangman!")
    print("let's start the game")
    print("You have only 6 tries to guess the word.")
    word = choose_word()
    guessed_letters = []
    incorrect_guesses = 0
    max_incorrect_guesses = 6

    while incorrect_guesses < max_incorrect_guesses:
        print("\nWord:", display_word(word, guessed_letters))
        guess = input("Guess a letter: ").lower()

        if guess in guessed_letters:
            print("You already guessed that letter! \ntry another one ")
        elif guess in word:
            print("Correct!")
            guessed_letters.append(guess)
        else:
            print("Incorrect!")
            incorrect_guesses += 1

        if set(word) <= set(guessed_letters):
            print("\nCongratulations! You guessed the word:", word)
            break

    if incorrect_guesses >= max_incorrect_guesses:
        print("\nSorry, you ran out of guesses. The word was:", word)

hangman()
