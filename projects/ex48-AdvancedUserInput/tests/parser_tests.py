# Nose test import also where assert_raises function lives
from nose.tools import *
from ex48 import parser
from ex48 import advanced_user_input as aui


def test_ParserError():
    pass


def test_Sentence():
    pass

# analyzing the peek function with the word eat. not sure why this works yet though.


def test_peek():
    word_list = aui.scan('eat')
    assert_equal(parser.peek(word_list), 'noun')
    assert_equal(parser.peek(None), None)
    # assert_equal(parser.peek(None), None)
    # assert_equal(aui.scan("go"), [('verb', 'go')])
    # result = aui.scan("go kill eat")
    # assert_equal(result, [('verb', 'go'),
    #                       ('verb', 'kill'),
    #                       ('verb', 'eat')])


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
