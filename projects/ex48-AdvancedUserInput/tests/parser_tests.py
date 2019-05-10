# Nose test import also where assert_raises function lives
from nose.tools import *
from ex48 import parser
from ex48 import advanced_user_input as aui

def test_ParserError():
    pass

def test_Sentence():
    pass
    # assert_equal(parser.Sentence("bear eat honey"),([('noun', 'bear'), ('verb', 'eat'), ('noun', 'honey')])
    # result = parser.Sentence("bear eat honey")
    # assert_equal(result, [('noun', 'bear'),
    #     ('verb', 'eat'),
    #     ('noun', 'honey')])

def test_peek():
    assert_equal(parser.peek("eat"), [("bear", "eat", "honey")])
    result = parser.peek("bear eat honey")
    assert_equal(result, [('verb', 'go'),
                          ('verb', 'kill'),
                          ('verb', 'eat')])

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