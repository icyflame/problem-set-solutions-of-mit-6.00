# Problem Set 5: Ghost
# Name: Siddharth
# Collaborators: None
# Time: 
#

import random

# -----------------------------------
# Helper code
# (you don't need to understand this helper code)
import string

WORDLIST_FILENAME = "words.txt"

def load_words():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print "Loading word list from file..."
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r', 0)
    # wordlist: list of strings
    wordlist = []
    for line in inFile:
        wordlist.append(line.strip().lower())
    print "  ", len(wordlist), "words loaded."
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


# (end of helper code)
# -----------------------------------

# Actually load the dictionary of words and point to it with 
# the wordlist variable so that it can be accessed from anywhere
# in the program.

wordlist = load_words()
from string import *

def is_valid_word_fragment(word_fragment):
    """returns if the given word fragment has any word starting with it"""
    word_fragment = word_fragment.lower()
    flag = True
    for i in range(len(wordlist)):
        if find(wordlist[i],word_fragment) is not -1:
            return True
        
    return False

def is_valid_word(word):
    """returns if the given word is a valid word"""
    word = word.lower()
    for i in range(len(wordlist)):
        if word == wordlist[i]:
            return True

    return False



def ghost():
    """implements a two player version of the classic word game GHOST"""
    
    print
    print 'Welcome to GHOST'
    print 'Player 1 will go first'
    print
    word_frag = ''
    t = 1
    ch = ''
    while 1:
        print
        print 'Current word fragment is:',word_frag
        print 'Current player is:',t
        
        ch = str(raw_input('Enter the letter:'))
        ch = ch.upper()

        if ch not in string.ascii_letters:   ##to check if the thing entered is a chrachter
            print 'This is not a valid charachter'
            print 'Try again!, Player ',t
            continue

        word_frag = word_frag + ch

        print 'Updated word fragment is:',word_frag

        if not is_valid_word_fragment(word_frag):
            print ' Player ',t,' loses as ',word_frag,' is not a valid word fragment'
            return

        if len(word_frag)>3 and is_valid_word(word_frag):
            print ' Player ',t,' loses as ',word_frag,' is a valid word'
            return

        print 'The charachter entered is fine, Player ',t
        
        
        if t == 1:
            t = 2
            continue
##necessary as if it is not there then the value of t
##will never change. as the second statement will assign
##the t as 1. as it was before and it will never be able to
##become 2
                    
        if t == 2:
            t = 1
            continue


