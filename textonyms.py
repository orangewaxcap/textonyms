def load_keypad(file):
    """
    Loads the key:character mapping from a text file.
    Format should be key, then space, then all characters for that key.
    Input: text file.
    Output: translation table produced by str.maketrans()
    """
    with open(file, 'r') as f:
        keys = [line.rstrip().lower() for line in f.readlines()]
    
    #create two lists for maketrans
    key_numbers = []
    key_letters = []
    
    for key in keys:
        if len(key) == 1: #that is, no letters assigned to it
            pass
        else:
            num, letts = key.split(' ')
            key_numbers.extend(num * len(letts))
            key_letters.extend(letts)
            
    table = str.maketrans(''.join(key_letters), ''.join(key_numbers))
        
    return table


def keypresses(string, table):
    """
    Make a textonym from a string and a lookup table.
    """
    return str.translate(string.lower(), table)


def create_dictionary(file, table):
    """
    Create a dictionary of word:textonym pairs.
    Input: line-delimited text file of words, plus table
    from load_keypad().
    Output: dictionary.
    """
    with open(file, 'r') as f:
        words = [line.rstrip() for line in f.readlines()]
    
    textonyms = [keypresses(word, table) for word in words]
    dictionary = dict(zip(words, textonyms))
    
    return dictionary


def textonyms(input_word, dictionary, table):
    """
    For a given word, find possible textonyms.
    Input: string, plus dictionary from create_dictionary(),
    plus table from load_keypad()
    Output: list of matching strings.
    """
    matches = [word for word,textonym in dictionary.items() if textonym == keypresses(input_word, table)]
    matches = [word for word in matches if word != input_word] #remove self-match
    return matches