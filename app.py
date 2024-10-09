import random
import sys
from termcolor import colored
import nltk

nltk.download("words")
from nltk.corpus import words

#! farruhdeveloper


# print menu
def print_menu():
    print("Let's play Worlde!")
    print("Type a 5-letter word and hit enter.\n")


word_list = words.words()
words_five = [word for word in word_list if len(word) == 5]

print(f"Number of 5-letter words available: {len(words_five)}")

print_menu()

play_again = ""

while play_again != "q":
    word = random.choice(words_five).lower()

    for attampt in range(1, 7):
        guess = input("Your guess: ").lower()

        for i in range(min(len(guess), 5)):
            if guess[i] == word[i]:
                print(colored(guess[i], "green"), end="")
            elif guess[i] in word:
                print(colored(guess[i], "yellow"), end="")
            else:
                print(guess[i], end="")

        print()

        if guess == word:
            print(f"You win! The word was {word}")
            break
        elif attampt == 6:
            print(f"You lose! The word was {word}")
            break


play_again = input("Play again? (q to quit) ")
