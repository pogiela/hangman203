from curses.ascii import isalpha
import random

# Task 1
word_list = ['banana', 'apple', 'pineaple', 'melon', 'grapefruit']
print(word_list)

# Task 2
word = random.choice(word_list)
print(word)

# Task 3
guess = input('Enter a single letter: ')

# Task 4
if len(guess) == 1 and guess.isalpha():
    print('Good guess!')
else:
    print('Oops! That is not a valid input.')