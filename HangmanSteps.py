#Step 1 

import random

#word_list = ["aardvark", "baboon", "camel"]
from hangman_words import word_list
from hangman_art import logo
print(logo)

#TODO-1 - Randomly choose a word from the word_list and assign it to a variable called chosen_word.
chosen_word = random.choice(word_list)
display = []
for n in range(0, len(chosen_word)):
    display.append("_")

#print(*display)


#TODO-2 - Ask the user to guess a letter and assign their answer to a variable called guess. Make guess lowercase.
lives = 6
letters_not_found = len(chosen_word)

from hangman_art import stages

while( (lives > 0) and (letters_not_found > 0 )):
    print(f"\nYou have {lives} lives remaining.")
    print(stages[lives])
    print(*display)
    guess = input("\nGuess a letter. ")
    guess.lower()

    if( (chosen_word.find(guess)) == -1):
        lives -= 1
        print(f"You guessed {guess}, that is not in the word. You lose a life.")

    for n in range(0, (len(chosen_word))):
        if(chosen_word[n] == guess):
            display[n] = guess
            letters_not_found -= 1

    #print(*display)

print("\nGame over.")
print("\nYour answer:")
print(*display)
print(f"\nThe word was: {chosen_word}.")