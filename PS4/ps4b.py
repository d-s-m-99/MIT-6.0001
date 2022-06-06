# Problem Set 4B
# Name: <your name here>
# Collaborators:
# Time Spent: x:xx

import string

### HELPER CODE ###
def load_words(file_name):
    '''
    file_name (string): the name of the file containing 
    the list of words to load    
    
    Returns: a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    '''
    print("Loading word list from file...")
    # inFile: file
    inFile = open(file_name, 'r')
    # wordlist: list of strings
    wordlist = []
    for line in inFile:
        wordlist.extend([word.lower() for word in line.split(' ')])
    print("  ", len(wordlist), "words loaded.")
    return wordlist

def is_word(word_list, word):
    '''
    Determines if word is a valid word, ignoring
    capitalization and punctuation

    word_list (list): list of words in the dictionary.
    word (string): a possible word.
    
    Returns: True if word is in word_list, False otherwise

    Example:
    >>> is_word(word_list, 'bat') returns
    True
    >>> is_word(word_list, 'asdf') returns
    False
    '''
    word = word.lower()
    word = word.strip(" !@#$%^&*()-_+={}[]|\:;'<>?,./\"")
    return word in word_list

def get_story_string():
    """
    Returns: a story in encrypted text.
    """
    f = open("story.txt", "r")
    story = str(f.read())
    f.close()
    return story

### END HELPER CODE ###

WORDLIST_FILENAME = 'words.txt'

class Message(object):
    def __init__(self, text):
        '''
        Initializes a Message object
                
        text (string): the message's text

        a Message object has two attributes:
            self.message_text (string, determined by input text)
            self.valid_words (list, determined using helper function load_words)
        '''
        self.message_text = text
        self.valid_words = load_words(WORDLIST_FILENAME)
# the variables in the initializer are private, in order to access them, we need to make a method that returns the private
# variable 
# can only access private variables in methods inside the same class, but to actually call them, we need to make a method to
#to return them
# the reason we have private variables is so that the user doesn't mess anything up, which would happen in the real world

# talk to caleb about setting private variables
    def get_message_text(self):
        '''
        Used to safely access self.message_text outside of the class
        
        Returns: self.message_text
        '''
        return self.message_text


    def get_valid_words(self):
        '''
        Used to safely access a copy of self.valid_words outside of the class.
        This helps you avoid accidentally mutating class attributes.
        
        Returns: a COPY of self.valid_words
        '''
        copy_valid_words = self.valid_words.copy()
        return copy_valid_words

    def build_shift_dict(self, shift):
        '''
        Creates a dictionary that can be used to apply a cipher to a letter.
        The dictionary maps every uppercase and lowercase letter to a
        character shifted down the alphabet by the input shift. The dictionary
        should have 52 keys of all the uppercase letters and all the lowercase
        letters only.        
        
        shift (integer): the amount by which to shift every letter of the 
        alphabet. 0 <= shift < 26

        Returns: a dictionary mapping a letter (string) to 
                 another letter (string). 
        '''
        #initialize an empty dictionary to hold the shift
        shifted_dict = {}
        #make the shift in the domain 0-25
# =============================================================================
#         shift = shift%25
# =============================================================================
        # function to construct the shift and add it to the dictionary
        #it's refractor of the below commmented code
        def add_shifted_to_dict(case_lett, shift):
            '''
            this function shifts down the charchters of the English alphabet by the value of input shift
            It builds the dictionary of shifted words, it takes set of alphbet
            and value of shifting of charchters
            keys of dictionary are English alphabet, both lower case and upper case
            values of the dictionary are the shifted down chacchters.
            
            ---------------
            case_lett: string, set of english alphabet either lower or upper case
            shift: int, value used to shift doen charchters
            '''
            for l in case_lett:
                shifted_index = case_lett.index(l) + shift
                if (shifted_index) > 25:
                    shifted_index = (shift-1) - (25- case_lett.index(l))
                shifted_dict[l] = case_lett[shifted_index]
        #shift lower case letters and adding them to the dictionary
        add_shifted_to_dict(string.ascii_lowercase, shift)
        #shift upper case letters and adding them to the dictionary
        add_shifted_to_dict(string.ascii_uppercase, shift)
        return shifted_dict


    def apply_shift(self, shift):
        '''
        Applies the Caesar Cipher to self.message_text with the input shift.
        Creates a new string that is self.message_text shifted down the
        alphabet by some number of characters determined by the input shift        
        
        shift (integer): the shift with which to encrypt the message.
        0 <= shift < 26

        Returns: the message text (string) in which every character is shifted
             down the alphabet by the input shift
        '''
        
        shifted_dict = self.build_shift_dict(shift)
        shifted_text = ""
        for i in self.message_text:
            if i in shifted_dict: 
                shifted_text += shifted_dict[i]
            if i not in shifted_dict:
                shifted_text += i
        return shifted_text
        

class PlaintextMessage(Message):
    def __init__(self, text, shift):
        '''
        Initializes a PlaintextMessage object        
        
        text (string): the message's text
        shift (integer): the shift associated with this message

        A PlaintextMessage object inherits from Message and has five attributes:
            self.message_text (string, determined by input text)
            self.valid_words (list, determined using helper function load_words)
            self.shift (integer, determined by input shift)
            self.encryption_dict (dictionary, built using shift)
            self.message_text_encrypted (string, created using shift)

        '''
        Message.__init__(self, text)
        self.shift = shift
        self.encryption_dict = self.build_shift_dict(self.shift) # why do we put self.shift here and not shift?
        self.message_text_encrypted = self.apply_shift(self.shift)


    def get_shift(self):
        '''
        Used to safely access self.shift outside of the class
        
        Returns: self.shift
        '''
        return self.shift

    def get_encryption_dict(self):
        '''
        Used to safely access a copy self.encryption_dict outside of the class
        
        Returns: a COPY of self.encryption_dict
        '''
        return self.encryption_dict.copy()

    def get_message_text_encrypted(self):
        '''
        Used to safely access self.message_text_encrypted outside of the class
        
        Returns: self.message_text_encrypted
        '''
        return self.message_text_encrypted

    def change_shift(self, shift):
        '''
        Changes self.shift of the PlaintextMessage and updates other 
        attributes determined by shift.        
        
        shift (integer): the new shift that should be associated with this message.
        0 <= shift < 26

        Returns: nothing
        '''
        self.encryption_dict = self.build_shift_dict(shift)
        self.message_text_encrypted = self.apply_shift(shift)



class CiphertextMessage(Message):
    def __init__(self, text):
        '''
        Initializes a CiphertextMessage object
                
        text (string): the message's text

        a CiphertextMessage object has two attributes:
            self.message_text (string, determined by input text)
            self.valid_words (list, determined using helper function load_words)
        '''
        Message.__init__(self, text)


    def decrypt_message(self):
        '''
        Decrypt self.message_text by trying every possible shift value
        and find the "best" one. We will define "best" as the shift that
        creates the maximum number of real words when we use apply_shift(shift)
        on the message text. If s is the original shift value used to encrypt
        the message, then we would expect 26 - s to be the best shift value 
        for decrypting it.

        Note: if multiple shifts are equally good such that they all create 
        the maximum number of valid words, you may choose any of those shifts 
        (and their corresponding decrypted messages) to return

        Returns: a tuple of the best shift value used to decrypt the message
        and the decrypted message text using that shift value
        '''
       #var for num of encrypted message words
        num_words = len(self.message_text.split())
        #initialize variable for holding max num of valid words
        max_val_words = 0
        #str var to keep the decrypted text of max valid words
        max_decrypted_text = ""
        #int var to hold shift of max valid words
        max_shift = 0
        #decrypt for every possible shift "s"
        for s in range(1,27):
            #track the current number of valid words
            current_num_val_words = 0
            #store the current shift
            current_shift = s
            #decrypt the message
            decrypted_msg = self.apply_shift(26-s)
            #split decrypted message in a list
            #test for validity
            for w in (decrypted_msg.split()):
                if is_word(self.valid_words, w):  
                #for each valid word, increment the current number of valid words by 1
                    current_num_val_words += 1
            #if the current number of valid words is equal to text words, return the function
            if current_num_val_words == num_words:
                return (current_shift, decrypted_msg)
            #if current number of valid words is bigger than max valid words, update max valid words, and decryted message of maximum words, and value of shift for this max valid words
            #otherwise, ignore this decryption and keep the last max decryption
            if current_num_val_words > max_val_words:
                max_val_words = current_num_val_words
                max_decrypted_text = decrypted_msg
                max_shift = current_shift
        #return tuple of text and key
        return (max_shift, max_decrypted_text)
if __name__ == "__main__":
    #Example test case (PlaintextMessage)
    plaintext = PlaintextMessage('hello', 2)
    print('Expected Output: jgnnq')
    print('Actual Output:', plaintext.get_message_text_encrypted())

    #Example test case (CiphertextMessage)
    ciphertext = CiphertextMessage('jgnnq')
    print('Expected Output:', (24, 'hello'))
    print('Actual Output:', ciphertext.decrypt_message())

    ciphertext = get_story_string()
    story = CiphertextMessage(ciphertext)
    elem_of_uncrypted_story = story.decrypt_message()
    uncry_story = elem_of_uncrypted_story[1]
    best_shift = elem_of_uncrypted_story[0]
    print("Actual Plaintext Story is \n", uncry_story)
    print("Best Shift is:", best_shift)
