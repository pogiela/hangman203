import random
from curses.ascii import isalpha


class Hangman:
    def __init__(self, word_list, num_lives=5):
        self.word_list = word_list # initiate list of words
        self.num_lives = num_lives # initiate number of lives the user has
        self.word = random.choice(self.word_list) # randomly selected word to be guessed from the word_list
        self.word_guessed = ['_' for letter in self.word] # list of the letters of the word, with _ for each letter not yet guessed. 
        self.num_letters = len(set(self.word)) # number of UNIQUE not guessed letters yet in the word
        self.list_of_guesses = [] # list of the guesses that have already been tried
    
        
    def check_guess(self, guess):
        # Convert the guessed letter to lower case
        guess = guess.lower()
        
        # Check if the letter is in the word
        if guess in self.word:
            print(f"Good guess! {guess} is in the word.")
            
            # Replace the '_' in the word_guessed list with the guessed letter
            for index, letter in enumerate(self.word):
                if letter == guess:
                    self.word_guessed[index] = letter
                    
            # Reduce the number of unique letters in the word still to be guessed  
            self.num_letters -= 1
        else:
            self.num_lives -= 1
            print(f"Sorry, {guess} is not in the word.")
            print(f"You have {self.num_lives} lives left.")
        

    def ask_for_input(self):
        # Ask the user for a letter until the user enters a valid letter
        while True:
            guess = input('Enter a single letter: ')
            # Check if the guess is a single alphanumeric character
            if len(guess) != 1 or not(guess.isalpha()):
                print('Invalid letter. Please, enter a single alphabetical character.')
            # Check if the guess is not one of the previous guesses
            elif guess in self.list_of_guesses:
                print('You already tried that letter!')
            # If the letter is valid
            else:
                # Call the function check_guess
                self.check_guess(guess)
                #  Add the guessed letter to the list_of_guesses
                self.list_of_guesses.append(guess)
                break
                
        
        
def play_game(word_list):
    # set default number of lives
    num_lives = 5
    # initiate the game
    game = Hangman(word_list, num_lives)
    print("Guess this word:")
    
    while True:
        # print the word to be guessed with '_' if letter not guessed yet
        print(game.word_guessed)
        # Check if the player has any lives left
        if game.num_lives == 0:
            # No lives left, game is lost
            print(f'You lost! The word was {game.word}')
            break
        # Check if there are any letters left to guess
        elif game.num_letters > 0:
            # letters still to guess, ask for input again
            game.ask_for_input()
        else:
            # No more letters to guess and still has lives, so winning
            print('Congratulations! You won!')
            break


if __name__ == '__main__':
    word_list = ['banana', 'apple', 'pineaple', 'melon', 'grapefruit', 'strawberry', 'blueberry']
    play_game(word_list)


