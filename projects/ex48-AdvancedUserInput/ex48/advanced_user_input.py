def scan(stuff):
    words = stuff.split()
    direction_words = ("north", "south", "east", "west")

    gamer_output = []
    for index in words:
        if index in direction_words:
            gamer_output.append(('direction', index))
    return(gamer_output)


stuff = "north west"

first_word = ('verb', 'go')
second_word = ('direction', 'north')
third_word = ('direction', 'west')
sentence = [first_word, second_word, third_word]
