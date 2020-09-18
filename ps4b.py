# Problem Set 4B
# Name: Mai Nguyen
# Collaborators: None 
# Time Spent: 4:00
# Late Days Used: 0

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
    word = word.strip(" !@#$%^&*()-_+={}[]|\:;'<>?,./\"")
    return word in word_list or word.swapcase() in word_list or word[0].lower()+word[1:] in word_list


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
    def __init__(self, input_text):
        '''
        Initializes a Message object

        input_text (string): the message's text

        a Message object has two attributes:
            self.message_text (string, determined by input text)
            self.valid_words (list, determined using helper function load_words)
        '''
        self.message_text=input_text
        self.valid_words=load_words('words.txt')


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
        
        return self.valid_words.copy()
        
    def make_shift_dict(self, input_shift):
        '''
        Creates a dictionary that can be used to apply a cipher to a letter.

        The dictionary maps every letter to a letter shifted down the extended 
        alphabet ("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ") by the 
        input shift. If 'a' is shifted down by 2, the result is 'c.'. IF 'z' is shifted
        down by 2 then the result is 'B'.

        The dictionary should contain 52 keys of all the uppercase letters
        and all the lowercase letters only, mapped to their shifted values.

        input_shift: the amount by which to shift every letter of the
        alphabet. 0 <= shift < 26*2 (52)

        Returns: a dictionary mapping letter (string) to
                 another letter (string).
        '''
        self.shift_dict={}
        # get string of both upper and lower case letters 
        upper_and_lower_letters=string.ascii_lowercase+string.ascii_uppercase
        # for every letter in the string 
        for i in range(len(upper_and_lower_letters)): 
            # if the shift doesnt roll over 
            if i+input_shift < 52:
                # dict key is original, value is the shifted letters 
                self.shift_dict[upper_and_lower_letters[i]]=upper_and_lower_letters[i+input_shift]
            # if the shift rolls over 
            else:
                self.shift_dict[upper_and_lower_letters[i]]=upper_and_lower_letters[input_shift-(52-i)]
        return self.shift_dict
    
    def apply_shift(self, shift_dict):
        '''
        Applies the Caesar Cipher to self.message_text with letter shift
        specified in shift_dict. Creates a new string that is self.message_text,
        shifted down the alphabet by some number of characters, determined by
        the shift value that shift_dict was built with.

        shift_dict: a dictionary with 52 keys, mapping
            lowercase and uppercase letters to their new letters
            (as built by make_shift_dict)

        Returns: the message text (string) with every letter shifted using the
            input shift_dict

        '''
        self.message_text_list=list(self.message_text)
        # generate a new list, get each element by looking up each item in self.message_text in the dictionary 
        # if item is not found, just return the original 
        self.message_text_list=[shift_dict.get(item,item) for item in self.message_text_list]
        str1=''
        return str1.join(self.message_text_list)

class PlaintextMessage(Message):
    def __init__(self, input_text, input_shift):
        '''
        Initializes a PlaintextMessage object.

        input_text (string): the message's text
        input_shift: the shift associated with this message

        A PlaintextMessage object inherits from Message. It has five attributes:
            self.message_text (string, determined by input text)
            self.valid_words (list, determined using helper function load_words)
            self.shift (integer, determined by input shift)
            self.encryption_dict (dictionary, built using the shift)
            self.encrypted_message_text (string, encrypted using self.encryption_dict)

        '''
        Message.__init__(self,input_text)
        self.shift=input_shift   # delete this line and replace with your code here
        self.encryption_dict = Message.make_shift_dict(self,self.shift)
        self.encrypted_message_text= Message.apply_shift(self, self.encryption_dict)
        

    def get_shift(self):
        '''
        Used to safely access self.shift outside of the class

        Returns: self.shift
        '''
        return self.shift 
     

    def get_encryption_dict(self):
        '''
        Used to safely access a copy of self.encryption_dict outside of the class

        Returns: a COPY of self.encryption_dict
        '''
        return self.encryption_dict.copy()

    def get_encrypted_message_text(self):
        '''
        Used to safely access self.encrypted_message_text outside of the class

        Returns: self.encrypted_message_text
        '''
        return self.encrypted_message_text
    

    def modify_shift(self, input_shift):
        '''
        Changes self.shift of the PlaintextMessage, and updates any other
        attributes that are determined by the shift.

        input_shift: the new shift that should be associated with this message.
        [0 <= shift < 52]

        Returns: nothing
        '''
        self.shift=input_shift
        self.encryption_dict = Message.make_shift_dict(self,self.shift)
        self.encrypted_message_text= Message.apply_shift(self, self.encryption_dict)


class EncryptedMessage(Message):
    def __init__(self, input_text):
        '''
        Initializes an EncryptedMessage object

        input_text (string): the message's text

        an EncryptedMessage object inherits from Message. It has two attributes:
            self.message_text (string, determined by input text)
            self.valid_words (list, determined using helper function load_words)
        '''
        Message.__init__(self,input_text) 

    def decrypt_message(self):
        '''
        Decrypts self.message_text by trying every possible shift value and
        finding the "best" one.

        We will define "best" as the shift that creates the max number of
        valid English words when we use apply_shift(shift) on the message text.
        If a is the original shift value used to encrypt the message, then
        we would expect (52 - a) to be the  value found for decrypting it.

        Note: if shifts are equally good, such that they all create the
        max number of valid words, you may choose any of those shifts
        (and their corresponding decrypted messages) to return.

        Returns: a tuple of the best shift value used to originally encrypt 
        the message (a) and the decrypted message text using that shift value
        '''
        # apply each possible combination of (input_shift)
        word_list=load_words('words.txt')
        number_valid_words=[]
        # check for each shift value 
        for i in range(0,52):
            # valid word counter for each case of shift value 
            valid_word=0
            # apply shift value 
            shifted_text=self.apply_shift(self.make_shift_dict(i))
            # count the number of valid English words in the decoded message
            for word in shifted_text.split():
                # is_word will ignore punctuation and other special characters when considering whether a word is valid.
                if is_word(word_list, word):
                    # count the valid word for this case 
                    valid_word+=1
            # get valid word value for all cases 
            number_valid_words.append(valid_word)
        # 52-a is the best shift value 
        a=number_valid_words.index(max(number_valid_words))
        decrypted_message=self.apply_shift(self.make_shift_dict(a))
        return (52-a, decrypted_message)
       
def test_plaintext_message():
    '''
    Write two test cases for the PlaintextMessage class here.
    Each one should handle different cases (see handout for
    more details.) Write a comment above each test explaining what
    case(s) it is testing.
    '''

#    #### Example test case (PlaintextMessage) #####

#    # This test is checking encoding a lowercase string with punctuation in it.
#    plaintext = PlaintextMessage('hello!', 2)
#    print('Expected Output: jgnnq!')
#    print('Actual Output:', plaintext.get_encrypted_message_text())

    # This test is checking encoding a lowercase and uppercase combined string with punctuation in it.
    plaintext = PlaintextMessage('hEllO!', 1)
    print('Expected Output: iFmmP!')
    print('Actual Output:', plaintext.get_encrypted_message_text())
    
    # This test is checking encoding all punctuations.
    plaintext = PlaintextMessage('!!!!,,,', 1)
    print('Expected Output: !!!!,,,')
    print('Actual Output:', plaintext.get_encrypted_message_text())

def test_encrypted_message():
    '''
    Write two test cases for the EncryptedMessage class here.
    Each one should handle different cases (see handout for
    more details.) Write a comment above each test explaining what
    case(s) it is testing.
    '''

#    #### Example test case (EncryptedMessage) #####

#   # This test is checking decoding a lowercase string with punctuation in it.
#    encrypted = EncryptedMessage('jgnnq!')
#    print('Expected Output:', (2, 'hello! or HELLO!'))
#    print('Actual Output:', encrypted.decrypt_message())

#This test is checking 
    encrypted = EncryptedMessage('dpowfstjoh')
    print('Expected Output:', ('1 or 27', 'conversing or CONVERSING'))
    print('Actual Output:', encrypted.decrypt_message())
#This test is checking decoding an upper case with punctuation on both sides 
    encrypted = EncryptedMessage('+)(*!DPOWFSTJOH')
    print('Expected Output:', ('+)(*!conversing'))
    print('Actual Output:', encrypted.decrypt_message())

def decode_story():
    '''
    Write your code here to decode the story contained in the file story.txt.
    Hint: use the helper function get_story_string and your EncryptedMessage class.

    Returns: a tuple containing (best_shift, decoded_story)

    '''
    story=EncryptedMessage(get_story_string())
    return story.decrypt_message()

if __name__ == '__main__':

    # Uncomment these lines to try running your test cases
    #test_plaintext_message()
    test_encrypted_message()

    # Uncomment these lines to try running decode_story_string()
    best_shift, story = decode_story()
    print("Best shift:", best_shift)
    print("Decoded story: ", story)

