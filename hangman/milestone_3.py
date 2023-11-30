from curses.ascii import isalpha
import random

def generate_random_word():
    word_list = ['banana', 'apple', 'pineaple', 'melon', 'grapefruit']
    print(word_list)
    word = random.choice(word_list)
    return word


def ask_for_input():
    guess = ''
    
    while True:
        guess = input('Enter a single letter: ')
        if len(guess) == 1 and guess.isalpha():
            break
        else:
            print('Invalid letter. Please, enter a single alphabetical character.')

    check_guess(guess)
    
    
def check_guess(guess):
    # Convert the guess into lower case.
    guess = guess.lower()
    
    # Check if the guess is in the randomly selected word     
    if guess in random_word:
        print(f"Good guess! {guess} is in the word.")
    else:
        print(f"Sorry, {guess} is not in the word. Try again.")
    
        

# generate a random word from the list
random_word = generate_random_word()
print(random_word)

# start the programme
ask_for_input()