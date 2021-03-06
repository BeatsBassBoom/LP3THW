# Nose test import also where assert_raises function lives
from nose.tools import *
from ex48.parser import *
from ex48.advanced_user_input import *

# analyzing the peek function with the word eat.
# not sure why this works yet though.


def test_peek():
    word_list = scan('princess go to the door')
    result = peek(word_list)
    expected_value = 'noun'
    assert_equal(result, expected_value)


def test_match():
    word_list = scan('princess go to the door')

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
    word_list = scan('princess go to the door')

    skip(word_list, 'stop')
    result = word_list
    word_list.pop(0)
    expected_value = word_list
    assert_equal(result, expected_value)


def test_parse_verb():
    word_list = scan('go to the door')

    expected_value = scan('go to the door').pop(0)
    result = parse_verb(word_list)
    assert_equal(result, expected_value)

    word_list_two = scan('princess go to the door')

    assert_raises(ParserError, parse_verb, word_list_two)


def test_parse_object():
    word_list = scan('princess go to the door')

    expected_value = scan('princess go to the door').pop(0)
    result = parse_object(word_list)
    assert_equal(result, expected_value)

    word_list_two = scan('go to the door')

    assert_raises(ParserError, parse_object, word_list_two)


def test_parse_subject():
    word_list = scan('princess go to the door')

    expected_value = scan('princess go to the door').pop(0)
    result = parse_subject(word_list)
    assert_equal(result, expected_value)

    word_list_two = scan('go to the door')

    assert_raises(ParserError, parse_object, word_list_two)
