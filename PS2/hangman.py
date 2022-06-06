# -*- coding: utf-8 -*-
"""
Created on Wed Apr 13 13:44:25 2022

@author: dsmil
"""

import random
import string

WORDLIST_FILENAME = "words.txt"


def load_words():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    #print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split() # makes words.txt into a list # (.split() makes a list)
    #print("  ", len(wordlist), "words loaded.")
    return wordlist
    


def choose_word(wordlist):
    """
    wordlist (list): list of words (strings)
    
    Returns a word from wordlist at random
    """
    return random.choice(wordlist)


wordlist = load_words()


def is_word_guessed(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing; assumes all letters are
      lowercase
    letters_guessed: list (of letters), which letters have been guessed so far;
      assumes that all letters are lowercase
    returns: boolean, True if all the letters of secret_word are in letters_guessed;
      False otherwise
    '''
    
    word_solver = secret_word # creating a new string that will be removing each letter correctly guessed in for loop
                                # creating a new string for this because we don't want to change secret_word in program
    for i in letters_guessed: # looping through letters guessed to see if they are in secret_word
        if i in secret_word: 
            word_solver = word_solver.replace(i, "") # removing the correct letter guessed
    return word_solver == ""


def get_guessed_word(secret_word, letters_guessed): 
    '''
    secret_word: string, the word the user is guessing
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string, comprised of letters, underscores (_), and spaces that represents
      which letters in secret_word have been guessed so far.
    '''
    # this code puts "_ " in secret_word where the letter is not correct and returns it
    secret_word_loop = list(secret_word)
    for i in range(len(secret_word_loop)):
        if secret_word_loop[i] not in letters_guessed:
            secret_word_loop[i] = "_ "
    return "".join(secret_word_loop)



def get_available_letters(letters_guessed):
    '''
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string (of letters), comprised of letters that represents which letters have not
      yet been guessed.
    '''

    delete_letter_from_alphabet = string.ascii_lowercase # this is a string of all lowercase letters to go through loop
    for i in range(len(letters_guessed)):
        if letters_guessed[i] in delete_letter_from_alphabet:
            delete_letter_from_alphabet = delete_letter_from_alphabet.replace(letters_guessed[i], "") # deleting letters we have guessed 
                                                                                                        #from lowercase letters of alphabet
    print("\nYou have not yet guessed these letters: %s" % delete_letter_from_alphabet)
    return delete_letter_from_alphabet # returns letters we have not guessed



def hangman(secret_word):
    '''
    secret_word: string, the secret word to guess.
    
    Starts up an interactive game of Hangman.
    
    * At the start of the game, let the user know how many 
      letters the secret_word contains and how many guesses s/he starts with.
      
    * The user should start with 6 guesses

    * Before each round, you should display to the user how many guesses
      s/he has left and the letters that the user has not yet guessed.
    
    * Ask the user to supply one guess per round. Remember to make
      sure that the user puts in a letter!
    
    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computer's word.

    * After each guess, you should display to the user the 
      partially guessed word so far.
    
    Follows the other limitations detailed in the problem write-up.
    '''

    n = len(secret_word)
    # need this to calculate score
    unique_letters = []
    for i in secret_word:
        if i not in unique_letters:
            unique_letters.append(i)
    num_unique_letters = len(unique_letters)
    # interactive game starts now
    print("Welcome to the Hangman game! \nI am thinking of a word that is ", n, " letters long.")
    num_guesses_left = 6
    letter_guess = []
    num_warnings = 3
    print("You have 3 warnings before losing a guess.")
    while not is_word_guessed(secret_word, letter_guess) and num_guesses_left > 0:
        print("\nYou have %d guesses left." % num_guesses_left)
        get_available_letters(letter_guess)
        print("This is what you have so far: ", get_guessed_word(secret_word, letter_guess))
        new_guess = str.lower(input("Input a new letter guess."))
        if not new_guess or new_guess not in string.ascii_lowercase:
            if num_warnings > 0:
                num_warnings -= 1
                print("That is not a valid letter input. You have %d warnings left." % num_warnings)
                print("--------------------------------------------------------------------------------")
            else:
                print("That is not a valid letter input. You have no warnings left so you lose a guess.")
                num_guesses_left -=1
                num_warnings = 3
                print("--------------------------------------------------------------------------------")
        elif new_guess in letter_guess:
            if num_warnings > 0:
                num_warnings -= 1
                print("You already guessed that letter. You have %d warnings left." % num_warnings)
                print("--------------------------------------------------------------------------------")
            else:
                print("You already guessed that letter. You have no warnings left so you lose a guess.")
                num_guesses_left -= 1
                num_warnings = 3
                print("--------------------------------------------------------------------------------")
        else:
            letter_guess.append(new_guess)
            if new_guess not in secret_word:
                print("\nThat letter is not in my word.")
                num_guesses_left -= 1
                print("--------------------------------------------------------------------------------")
            else:
                print("Good guess!")
                print("--------------------------------------------------------------------------------")
        
    if num_guesses_left == 0:
        print("Sorry, you lost. the word is: %s" % secret_word)
    
    if is_word_guessed(secret_word, letter_guess):
        print("Congratulations! You won. Your score is: %d " % (num_unique_letters * num_guesses_left))
        
    

if __name__ == "__main__":

    
    secret_word = choose_word(wordlist)
    hangman(secret_word)
    print(secret_word)

    

