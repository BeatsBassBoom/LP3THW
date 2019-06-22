# Scan function to split and parse the user input.
def scan(word_play):
    words = word_play.split()
    # Store to contain all the possible user input options.
    direction_words = ("north", "south", "east", "west")
    verb_words = ("go", "kill", "eat")
    stop_words = ("the", "in", "of", "to")
    noun_Words = ("bear", "princess", "honey")

    # List that will be used to categorize all the user input to 
    # return later in the test.
    gamer_output = []
    # Loop across all the split words for category association.
    for index in words:
        if index in direction_words:
            gamer_output.append(('direction', index))
        elif index in verb_words:
            gamer_output.append(('verb', index))
        elif index in stop_words:
            gamer_output.append(('stop', index))
        elif index in noun_Words:
            gamer_output.append(('noun', index))
        # Check if the current value is a number.
        elif index.isdigit() and len(index) <= 5:
            gamer_output.append(('number', int(index)))
        else:
            gamer_output.append(('error', index))
    return(gamer_output)


# stuff = input('> ')
word_play = "go north west bear east"

# first_word = ('verb', 'go')
# second_word = ('direction', 'north')
# third_word = ('direction', 'west')
# sentence = [first_word, second_word, third_word]
