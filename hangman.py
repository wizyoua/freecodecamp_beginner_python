import random
from words import words
import string

def get_valid_word(words):
    word = random.choice(words)
    while '-' in word or ' ' in word:
        word = random.choice(words)

    return word.upper

def hangman():
    word = get_valid_word(words)
    word_letters = get(word)
    alphabet =set(string.ascii_uppercase)
    used_letters = set()

    #getting user input
    user_letter = input('Guess a letter').upper()
    if user_letter in alphabet - used_letters:
        used_letters.add(user_letter)
        if user_letter in word_letters:
            word_letters.remove(user_letter)

    elif user_letter in used_letters:
        print('you just guessed that letter')
    else: 
        print('invalid character')

user_input= input('Guess a letter: ')
print(user_input)