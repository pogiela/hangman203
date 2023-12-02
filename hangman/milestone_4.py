import random
from curses.ascii import isalpha

word_list = ['banana', 'apple', 'pineaple', 'melon', 'grapefruit']

class Hangman:
    def __init__(self, word_list, num_lives=5):
        self.word_list = word_list # list of words
        self.num_lives = num_lives # number of lives the user has
        self.word = random.choice(self.word_list) # randomly selected word to be guessed from the word_list
        self.word_guessed = ['_' for letter in self.word] # list of the letters of the word, with _ for each letter not yet guessed. 
        self.num_letters = len(set(self.word)) # number of UNIQUE not guessed letters yet in the word
        self.list_of_guesses = [] # list of the guesses that have already been tried
    
    
    def check_guess(self, guess):
        # Convert the guessed letter to lower case
        guess = guess.lower()
        
        # Check if the guess is in the randomly selected word     
        if guess in self.word:
            print(f"Good guess! {guess} is in the word.")
            for index, letter in enumerate(self.word):
                if letter == guess:
                    self.word_guessed[index] = letter
                    
            self.num_letters -= 1
        else:
            self.num_lives -= 1
            print(f"Sorry, {guess} is not in the word.")
            print(f"You have {self.num_lives} lives left.")
        

    def ask_for_input(self):
        while True:
            guess = input('Enter a single letter: ')
            if len(guess) != 1 or not(guess.isalpha()):
                print('Invalid letter. Please, enter a single alphabetical character.')
            elif guess in self.list_of_guesses:
                print('You already tried that letter!')
            else:
                self.check_guess(guess)
                self.list_of_guesses.append(guess)
                print(self.num_letters)
                print(self.list_of_guesses)
                print(self.word_guessed)
                
        
        
        
    
hangman = Hangman(word_list)
print(hangman.word)
print(hangman.num_letters)
print(hangman.list_of_guesses)
print(hangman.word_guessed)
hangman.ask_for_input()