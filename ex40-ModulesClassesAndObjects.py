# Modules, Classes, and Objects

'''
mystuff = {'apple': "I AM APPLES!"}
print(mystuff['apple'])

# this goes in mystuff.py
def apple():
    print("I AM APPLES!")

# this is just a variable
tangerine = "Living reflection of a dream"

import mystuff
mystuff.apple()
print(mystuff.tangerine)

mystuff['apple'] # get apple from dict
mystuff.apple() # get apple from the module
mystuff.tangerine # same thing, it's just a variable


class MyStuff(object):

    def __init__(self):
        self.tangerine = "And now a thousand years between"

    def apple(self):
        print("I AM CLASSY APPLES!")


thing = MyStuff()
thing.apple()
print(thing.tangerine)


# Getting things from things
# dict style
mystuff['apples']

# module style
mystuff.apples()
print(mystuff.tangerine)

# class style
thing = MyStuff()
thing.apples()
print(thing.tangerine)
'''

# A first class example

class Song(object):
    def __init__(self, lyrics):
        self.lyrics = lyrics

    def sing_me_a_song(self):
        for line in self.lyrics:
            print(line)

happy_bday = Song(["Happy birthday to you",
                   "I don't want to get sued",
                   "So I'll stop right there"])

bulls_on_parade = Song(["They rally around the family",
                        "With pockets full of shells"])

x_gon_give_it_to_ya = Song(["Woof Woof Woof",
                            "X Gon Give It To Ya"])

hey_ya = Song(["Heeeeyyyy Yaaaaa",
               "Shake it like a polaroid picture"])

happy_bday.sing_me_a_song()

bulls_on_parade.sing_me_a_song()

x_gon_give_it_to_ya.sing_me_a_song()

hey_ya.sing_me_a_song()

bday_lyrics = "Happy birthday to you I don't want to get sued So I'll stop right there"