from curses.ascii import isalpha
import random

def generate_random_word():
    word_list = ['banana', 'apple', 'pineaple', 'melon', 'grapefruit']
    word = random.choice(word_list)
    return word

def get_user_input():
    guess = input('Enter a single letter: ')

    if len(guess) == 1 and guess.isalpha():
        print('Good guess!')
    else:
        print('Oops! That is not a valid input.')
        get_user_input()
        
random_word = generate_random_word()
print(random_word)

get_user_input()