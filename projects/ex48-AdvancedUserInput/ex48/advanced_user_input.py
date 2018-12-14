
# north, south, east, west, down, up, left, right, back


def directions(words):
    direction_words = ("north", "south", "east", "west")
    direction_index = 0
    while direction_index < len(direction_words):
        if direction_words[direction_index] in words.split():
            return([('direction', direction_words[direction_index])])
        direction_index += 1

# go, stop, kill, eat


def verbs():
    pass

# the, in, of, from, at, it


def stop_words():
    pass

# door, bear, princess, cabinet


def nouns():
    pass

# any string of 0 through 9 characters


def numbers():
    pass


def scan(words):
    second_word = ('direction', 'north')
    return([second_word])


stuff = " Hi my name is north west down go"
words = stuff.split()

first_word = ('verb', 'go')
second_word = ('direction', 'north')
third_word = ('direction', 'west')
sentence = [first_word, second_word, third_word]
