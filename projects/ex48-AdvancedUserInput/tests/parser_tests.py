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
    word_list = scan('princess go to the door')
    # word_list_two = scan('princess go to the door')

    first_result = match(word_list, 'noun')
    second_result = match(word_list, 'verb')
    third_result = match(scan(''), ' ')
    fourth_result = match(word_list, 'stop')

    first_expected_value = ('noun', 'princess')
    second_expected_value = ('verb', 'go')
    third_expected_value = None
    fourth_expected_value = ('stop', 'to')
    
    assert_equal(first_result, first_expected_value)
    assert_equal(second_result, second_expected_value)
    assert_equal(third_result, third_expected_value)
    assert_equal(fourth_result, fourth_expected_value)


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