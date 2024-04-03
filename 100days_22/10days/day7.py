"""Hangman"""

import random

stages = [r'''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', r'''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', r'''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', r'''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', r'''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', r'''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', r'''
  +---+
  |   |
      |
      |
      |
      |
=========
''']

logo = r''' 
 _                                             
| |                                            
| |__   __ _ _ __   __ _ _ __ ___   __ _ _ __  
| '_ \ / _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
| | | | (_| | | | | (_| | | | | | | (_| | | | |
|_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                    __/ |                      
                   |___/    '''


def display_word(g_letters, word=""):
    """Wyswietlanie slowa do zgadniecia"""
    # mozna bylo za pomoca jednej listy z _ lub porownywania liter indx
    for letter in word:
        if letter in g_letters:
            print(letter, end='')
        else:
            print('_', end='')
    print()


def display_lives(lives):
    print("Lives:", lives)
    print(stages[len(stages) - lives - 1])


def guess_letter():
    guess = "WRONG_ANSWER"
    while len(guess) != 1 or not guess.isalpha():
        guess = input('Provide your guess: ')
        if len(guess) != 1 or not guess.isalpha():
            print('Wrong input please try again!')
    return guess.lower()


def welcome_msg():
    print(logo)
    print("Hangman Game")
    print("Word to guess: ")
    display_word(guessed_letters, chosen_word)
    display_lives(player_lives)


if __name__ == "__main__":
    word_list = ['apple', 'banana', 'tiger']
    guessed_letters = []  # mozna bylo za pomoca mapy
    chosen_word = random.choice(word_list)
    game_on = True
    player_lives = 6

    welcome_msg()

    while game_on:
        display_word(guessed_letters, chosen_word)
        guessed_letter = guess_letter()

        if guessed_letter in chosen_word and guessed_letter not in guessed_letters:
            print('You have guessed a letter!')
            for i in range(chosen_word.count(guessed_letter)):
                guessed_letters.append(guessed_letter)
        else:
            player_lives -= 1
            if player_lives == 0:
                display_lives(player_lives)
                print('You got hanged!')
                game_on = False
                break

        display_lives(player_lives)

        # a mozna bylo miec ta jedna list z _ i sprawdzic czy sa _
        if len(guessed_letters) == len(chosen_word):
            check1 = ''.join(sorted(guessed_letters))
            check2 = ''.join(sorted(chosen_word))
            if check1 == check2:
                print('Congratulations! You won!')
                game_on = False
                break
