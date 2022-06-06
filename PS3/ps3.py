# -*- coding: utf-8 -*-
"""
Created on Fri Apr 22 13:39:18 2022

@author: dsmil
"""

# Word Game

import math
import random
import string

VOWELS = 'aeiou'
CONSONANTS = 'bcdfghjklmnpqrstvwxyz'
HAND_SIZE = 7
ALL_LETTERS = VOWELS + CONSONANTS
SCRABBLE_LETTER_VALUES = {
    'a': 1, 'b': 3, 'c': 3, 'd': 2, 'e': 1, 'f': 4, 'g': 2, 'h': 4, 'i': 1, 'j': 8, 'k': 5, 'l': 1, 'm': 3, 'n': 1, 'o': 1, 'p': 3, 'q': 10, 'r': 1, 's': 1, 't': 1, 'u': 1, 'v': 4, 'w': 4, 'x': 8, 'y': 4, 'z': 10, '*': 0
}



WORDLIST_FILENAME = "words.txt"

def load_words():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # wordlist: list of strings
    wordlist = []
    for line in inFile:
        wordlist.append(line.strip().lower())
    print("  ", len(wordlist), "words loaded.")
    return wordlist

def get_frequency_dict(sequence):
    """
    Returns a dictionary where the keys are elements of the sequence
    and the values are integer counts, for the number of times that
    an element is repeated in the sequence.

    sequence: string or list
    return: dictionary
    """
    
    # freqs: dictionary (element_type -> int)
    freq = {}
    for x in sequence:
        freq[x] = freq.get(x,0) + 1
    return freq
	

def get_word_score(word, n):
    """
    Returns the score for a word. Assumes the word is a
    valid word.

    You may assume that the input word is always either a string of letters, 
    or the empty string "". You may not assume that the string will only contain 
    lowercase letters, so you will have to handle uppercase and mixed case strings 
    appropriately. 

	The score for a word is the product of two components:

	The first component is the sum of the points for letters in the word.
	The second component is the larger of:
            1, or
            7*wordlen - 3*(n-wordlen), where wordlen is the length of the word
            and n is the hand length when the word was played

	Letters are scored as in Scrabble; A is worth 1, B is
	worth 3, C is worth 3, D is worth 2, E is worth 1, and so on.

    word: string
    n: int >= 0
    returns: int >= 0
    """
    word_for_loop = word.lower()
    first_comp = 0
    
    for i in word_for_loop:
        first_comp += SCRABBLE_LETTER_VALUES[i]
    second_comp = (7 * len(word)) - (3 * (n - len(word)))
    if second_comp < 1:
        second_comp = 1
    score = first_comp * second_comp
    print(score)
    return score

    
def display_hand(hand):
    """
    Displays the letters currently in the hand.

    For example:
       display_hand({'a':1, 'x':2, 'l':3, 'e':1})
    Should print out something like:
       a x x l l l e
    The order of the letters is unimportant.

    hand: dictionary (string -> int)
    """
    your_hand = ""
    for letter in hand.keys():
        for j in range(hand[letter]):
            your_hand = your_hand +  letter + " "
                   # print all on the same line
    return your_hand                              


def deal_hand(n):
    """
    Returns a random hand containing n lowercase letters.
    ceil(n/3) letters in the hand should be VOWELS (note,
    ceil(n/3) means the smallest integer not less than n/3).

    Hands are represented as dictionaries. The keys are
    letters and the values are the number of times the
    particular letter is repeated in that hand.

    n: int >= 0
    returns: dictionary (string -> int)
    """
    
    hand={}
    num_vowels = int(math.ceil(n / 3))

    for i in range(num_vowels):
        if i == (num_vowels - 1):
            x = "*"
            hand[x] = 1
        else:
            x = random.choice(VOWELS)
            hand[x] = hand.get(x, 0) + 1
    
    for i in range(num_vowels, n):    
        x = random.choice(CONSONANTS)
        hand[x] = hand.get(x, 0) + 1
    
    return hand

def update_hand(hand, word):
    """
    Does NOT assume that hand contains every letter in word at least as
    many times as the letter appears in word. Letters in word that don't
    appear in hand should be ignored. Letters that appear in word more times
    than in hand should never result in a negative count; instead, set the
    count in the returned hand to 0 (or remove the letter from the
    dictionary, depending on how your code is structured). 

    Updates the hand: uses up the letters in the given word
    and returns the new hand, without those letters in it.

    Has no side effects: does not modify hand.

    word: string
    hand: dictionary (string -> int)    
    returns: dictionary (string -> int)
    """
    word = word.lower()
    hand_for_loop = hand.copy()
    hand_keys = hand_for_loop.keys()
    # loop through each letter in word
    for letter in word: 
        # seeing if each letter in the word is in the hand
        if letter in hand_keys:
            # if the hand has multiple of the same letter, then it will substract one 
            # from the key's value in the dictionary
            if hand_for_loop[letter] > 0:
                hand_for_loop[letter] -= 1
            else:
                del hand_for_loop[letter]
    return hand_for_loop


# define a function that returns a list of all the possible words that could be made by replacing the asterisk with a vowel
def possible_words_with_asterisk(word, hand, word_list): # For some reason this fails when i call it, but when i put the same code
                                                        # in the loop, it works
    """
    When this function is called, we are in a loop that meets the condition that an asterisk ('*')
    is in the word. This function loops through the vowels and replaces the asterisk in the word
    with the vowel to then see if that word is in word_list. If it is, then it is added to a list
    of potential words that the word with the asterisk could be. If the length of the potential 
    list of words is greater than one, then returns True, else, returns False because the word
    the user input is not a valid word
    
    word : string
    hand : dictionary (string -> int)
    word_list : list of lowercase strings
    returns : boolean
    """
    lower_case_word = word.lower()
    possible_words_from_asterisk = []
    hand_keys = hand.keys()
    asterisk_index = lower_case_word.find('*')
    for vowel in VOWELS: # trying each vowel in place of asterisk to see if input could be a valid word
        hand_for_loop = hand.copy()
        lower_case_word = word.lower()
        potential_word = lower_case_word.replace('*', vowel)
        hand_for_loop['*'] -= 1
        if potential_word in word_list:
            for char in range(len(potential_word)): #looping through each letter of the attempted word, which is a real word, to see if each letter is in our hand
                if char != asterisk_index:
                     # this passed
                    if potential_word[char] in hand_keys:
                        hand_for_loop[potential_word[char]] -= 1
                        if potential_word[char] == potential_word[-1] and hand_for_loop[potential_word[char]] >= 0:
                            possible_words_from_asterisk.append(potential_word)
                            
                        if hand_for_loop[potential_word[char]] < 0: # running out of letters in the hand will return False
                            continue
        

    return (len(possible_words_from_asterisk) > 0)


def is_valid_word(word, hand, word_list):
    """
    Returns True if word is in the word_list and is entirely
    composed of letters in the hand. Otherwise, returns False.
    Does not mutate hand or word_list.
   
    word: string
    hand: dictionary (string -> int)
    word_list: list of lowercase strings
    returns: boolean
    """
    word_lowercase = word.lower() #takes into account capital letters (just converts them to lowercase
    hand_keys = hand.keys()
    hand_for_loop = hand.copy() # don't want to mutate original dictionary of the hand
    if "*" in word_lowercase: 
        asterisk_index = word_lowercase.find('*')
        possible_words_from_asterisk = []
        for vowel in VOWELS: # trying each vowel in place of asterisk to see if input could be a valid word
            potential_word = word_lowercase.replace('*', vowel)
            hand_for_loop['*'] -= 1
            if potential_word in word_list: # checks if this is a valid word
                for char in range(len(potential_word)): #looping through each letter of the attempted word, which is a real word, to see if each letter is in our hand
                    if char != asterisk_index:
                        if potential_word[char] in hand_keys:
                            hand_for_loop[potential_word[char]] -= 1
                            if potential_word[char] == potential_word[-1] and hand_for_loop[potential_word[char]] >= 0:
                                possible_words_from_asterisk.append(potential_word)
                                
                            if hand_for_loop[potential_word[char]] < 0: # running out of letters in the hand will return False
                                continue
        if len(possible_words_from_asterisk) > 0:
            return True
        else:
            return False
# =============================================================================
#         possible_words_with_asterisk(word_lowercase, hand, word_list)
# =============================================================================
        # is this returning False?
    elif word_lowercase not in word_list: # checks if this is a valid word
        return False
    else:
        for letter in word_lowercase: #looping through each letter of the attempted word, which is a real word, to see if each letter is in our hand
            if letter in hand_keys:
                hand_for_loop[letter] -= 1
                if hand_for_loop[letter] < 0: # running out of letters in the hand will return False
                    print("Please enter a word that is in your hand.")
                    return False
            else: 
                return False
        return True

                

def calculate_handlen(hand):
    """ 
    Returns the length (number of letters) in the current hand.
    
    hand: dictionary (string-> int)
    returns: integer
    """
    value = 0
    for key in hand.keys():
        value += hand[key]
    return value


def play_hand(hand, word_list):

    """
    Allows the user to play the given hand, as follows:

    * The hand is displayed.
    
    * The user may input a word.

    * When any word is entered (valid or invalid), it uses up letters
      from the hand.

    * An invalid word is rejected, and a message is displayed asking
      the user to choose another word.

    * After every valid word: the score for that word is displayed,
      the remaining letters in the hand are displayed, and the user
      is asked to input another word.

    * The sum of the word scores is displayed when the hand finishes.

    * The hand finishes when there are no more unused letters.
      The user can also finish playing the hand by inputing two 
      exclamation points (the string '!!') instead of a word.

      hand: dictionary (string -> int)
      word_list: list of lowercase strings
      returns: the total score for the hand
      
    """
    
    updated_hand = hand.copy()
    score_total = 0
    num_char = calculate_handlen(updated_hand)
    while num_char > 0:
        print("This is your hand: ", display_hand(updated_hand))
        word = input("Enter word, or '!!' to indicate that you are finished: \n")
        if is_valid_word(word, updated_hand, word_list):
            score = get_word_score(word, calculate_handlen(updated_hand))
            print("Score for - " + word + " - is %d" %  score)
            score_total += score
        elif word == "!!":
            break
        else:
            print("Please enter a valid word. You lose the characters that you input as a penalty \
                   for inputting an invalid word.")

        updated_hand = update_hand(updated_hand, word)# is this sus?
        num_char = calculate_handlen(updated_hand)

    print("Game is over. \n Your score for the game is %d" % score_total)
    return score_total


def substitute_hand(hand, letter):
    """ 
    Allow the user to replace all copies of one letter in the hand (chosen by user)
    with a new letter chosen from the VOWELS and CONSONANTS at random. The new letter
    should be different from user's choice, and should not be any of the letters
    already in the hand.

    If user provide a letter not in the hand, the hand should be the same.

    Has no side effects: does not mutate hand.

    For example:
        substitute_hand({'h':1, 'e':1, 'l':2, 'o':1}, 'l')
    might return:
        {'h':1, 'e':1, 'o':1, 'x':2} -> if the new letter is 'x'
    The new letter should not be 'h', 'e', 'l', or 'o' since those letters were
    already in the hand.
    
    hand: dictionary (string -> int)
    letter: string
    returns: dictionary (string -> int)
    """
    sub_hand = hand.copy()
    all_letters = ALL_LETTERS
    # removing characters in the key from the alphabet to randomly choose from altered alphabet to replace letter
    for char in sub_hand.keys():
        all_letters = all_letters.replace(char, "")
    sub_hand[random.choice(all_letters)] = sub_hand[letter]
    del sub_hand[letter]
    return sub_hand
       
    
def play_game(word_list):
    """
    Allow the user to play a series of hands

    * Asks the user to input a total number of hands

    * Accumulates the score for each hand into a total score for the 
      entire series
 
    * For each hand, before playing, ask the user if they want to substitute
      one letter for another. If the user inputs 'yes', prompt them for their
      desired letter. This can only be done once during the game. Once the
      substitue option is used, the user should not be asked if they want to
      substitute letters in the future.

    * For each hand, ask the user if they would like to replay the hand.
      If the user inputs 'yes', they will replay the hand and keep 
      the better of the two scores for that hand.  This can only be done once 
      during the game. Once the replay option is used, the user should not
      be asked if they want to replay future hands. Replaying the hand does
      not count as one of the total number of hands the user initially
      wanted to play.

            * Note: if you replay a hand, you do not get the option to substitute
                    a letter - you must play whatever hand you just had.
      
    * Returns the total score for the series of hands

    word_list: list of lowercase strings
    """
    num_hands = int(input("Enter total number of hands: "))
    num_replay = 0
    total_score = 0
    for i in range(1, num_hands + 1):
        print("This is hand #%s" % i)
        hand = deal_hand(HAND_SIZE)
        print("Current hand: \n", display_hand(hand))
        option_to_sub = input("Would you like to substitute a letter? ").lower()
        if option_to_sub == "yes":
            letter = input("Which letter would you like to replace? ")
            sub_hand = substitute_hand(hand, letter)
            score = play_hand(sub_hand, word_list)
        else:
            score = play_hand(hand, word_list)
        if num_replay == 0:
            option_to_replay = input("Would you like to replay the hand? You can only do this once. ").lower()
            if option_to_replay == "yes":
                num_replay += 1
                new_score = play_hand(hand, word_list)
                if new_score > score: # taking the higher score of the replay
                    score = new_score
        total_score += score
    return total_score

    

if __name__ == '__main__':
    word_list = load_words()
    print("Score for all hands: ", play_game(word_list))

