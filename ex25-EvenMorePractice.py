def break_words(stuff):
    # This is known as a documentation comment which will display if I ask for help from the function.
    """This function will break up words for us."""
    # This line splits each word when it detects a space and will place the word in single quotes.
    words = stuff.split(' ')
    return words

def sort_words(words):
    """Sorts the words."""
    # This return calls the function sorted which will sort the word list
    # by ascending order.
    return sorted(words)

def print_first_word(words):
    """Prints te first word after popping it off."""
    # Calls the pop function which takes off the word at the first index.
    word = words.pop(0)
    print(word)

def print_last_word(words):
    """Prints the last word after popping it off."""
    # Calls the pop function which takes off the word at the last index.
    word = words.pop(-1)
    print(word)

def sort_sentence(sentence):
    """Takes in a full sentence and returns the sorted words."""
    # Calls the break words function above to split the sentence.
    words = break_words(sentence)
    # Calls the sort words function above to order the list in ascending order.
    return sort_words(words)

def print_first_and_last(sentence):
    """Prints the first and last words of the sentence."""
    words = break_words(sentence)
    print_first_word(words)
    print_last_word(words)

def print_first_and_last_sorted(sentence):
    """Sorts the words then prints the first and last one."""
    words = sort_sentence(sentence)
    print_first_word(words)
    print_last_word(words)