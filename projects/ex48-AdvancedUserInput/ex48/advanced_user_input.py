def scan(stuff):
    words = stuff.split()
    direction_words = ("north", "south", "east", "west")
    verb_words = ("go", "kill", "eat")
    stop_words = ("the", "in", "of")
    noun_Words = ("bear", "princess")

    gamer_output = []
    for index in words:
        if index in direction_words:
            gamer_output.append(('direction', index))
        elif index in verb_words:
            gamer_output.append('verb', index)
        elif index in stop_words:
            gamer_output.append(('stop', index))
        elif index in noun_Words:
            gamer_output.append(('noun', index))
        elif index.isdigit() and len(index) <= 5:
            gamer_output.append(('number', int(index)))
        else:
            gamer_output.append(('error', index))
    return(gamer_output)


stuff = "north west"

first_word = ('verb', 'go')
second_word = ('direction', 'north')
third_word = ('direction', 'west')
sentence = [first_word, second_word, third_word]


# #Set up datastructure
# direction = ["north", "east", "south", "west",
#              "up", "right", "down", "left", "back"]
# verb = ["go", "stop", "kill", "eat"]
# stop = ["the", "in", "of", "from", "at", "it"]
# noun = ["door", "bear", "princess", "cabinet"]
# vocabulary = [(direction, 'direction'), (verb, 'verb'),
#               (stop, 'stop'), (noun, 'noun')]


# def scan(sentence):
#     #searches the words in the datastructure, if not found checks if it is an integer, if not returns error.
#     results = []
#     words = sentence.split()

#     for word in words:
#         found = False
#         for category in vocabulary:
#             if word.lower() in category[0]:
#                 results.append((category[1], word))
#                 found = True
#             else:
#                 pass
#         if found is False and isInt_str(word) is True:
#             results.append(('number', int(word)))
#         elif found is False and isInt_str(word) is False:
#             results.append(('error', word))
#         elif found is True:
#             pass
#         else:
#             print(
#                 "I'm terribly sorry, but something you entered is neither a word nor a number.")
#     return results


# def isInt_str(string):
#     #returns True or False if string equals an integer. (i.e. 2 = True, 2*-2 = True 2**0,5 = False)
#     string = str(string).strip()
#     return string == '0' or (string if string.find('..') > -1 else string.lstrip('-+').rstrip('0').rstrip('.')).isdigit()
