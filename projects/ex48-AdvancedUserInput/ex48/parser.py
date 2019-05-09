#ex49 Making Sentences
# This file is where we are implementing exercise 49

# Parser class to throw my own exceptions.
class ParserError(Exception):
    pass


class Sentence(object):

    def __init__(self, subject, verb, obj):
        # remember we take ('noun','princess') tuples and convert them
        self.subject = subject[1]
        self.verb = verb[1]
        self.object = obj[1]

# Peeks at a list of words and returns its type of word.
def peek(word_list):
    if word_list:
        word = word_list[0]
        return word[0]
    else:
        return None

# Confirms the word is the correct type, takes it out of the list and returns the word.
def match(word_list, expecting):
    if word_list:
        word = word_list.pop(0)

        if word[0] == expecting:
            return word
        else:
            return None
    else:
        return None

# Skips words that are not useful to the sentence (stop words)
def skip(word_list, word_type):
    while peek(word_list) == word_type:
        match(word_list, word_type)

# Handles parsing verbs
def parse_verb(word_list):
    skip(word_list, 'stop')

    if peek(word_list) == 'verb':
        return match(word_list, 'verb')
    else:
        raise ParserError("Expected a verb next.")

# Skip any words, peek ahead to see if next word is a verb, if not raise error, otherwise match the word and take it off the list.
def parse_object(word_list):
    skip(word_list, 'stop')
    next_word = peek(word_list)
    if next_word == 'noun':
        return match(word_list, 'noun')
    elif next_word == 'direction':
        return match(word_list, 'direction')
    else:
        raise ParserError("Expected a noun or direction next.")

# Skip stop words, peek ahead to see if sentence is corret. 
def parse_subject(word_list):
    skip(word_list, 'stop')
    next_word = peek(word_list)

    if next_word == 'noun':
        return match(word_list, 'noun')
    elif next_word == 'verb':
        return ('noun', 'player')
    else:
        raise ParserError("Expected a verb next.")


def parse_sentence(word_list):
    subj = parse_subject(word_list)
    verb = parse_verb(word_list)
    obj = parse_object(word_list)

    return Sentence(subj, verb, obj)
