# Nose test import also where assert_raises function lives
from nose.tools import *
from ex48.parser import *
from ex48.advanced_user_input import *


def test_ParserError():
    pass


def test_Sentence():
    pass

# analyzing the peek function with the word eat. 
# not sure why this works yet though.
def test_peek():
    word_list = scan('princess go to the door')
    result = peek(word_list)
    expected_value = 'noun'
    assert_equal(result, expected_value)


def test_match():
    pass


def test_skip():
    pass


def test_parse_verb():
    pass


def test_parse_object():
    pass


def test_parse_subject():
    pass


def test_parse_sentence():
    pass