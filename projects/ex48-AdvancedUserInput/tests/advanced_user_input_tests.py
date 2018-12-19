# Nose test import
from nose.tools import *
# Importing the ex48 user input file.
from ex48 import advanced_user_input as aui


def test_directions():
    assert_equal(aui.scan("north"), [('direction', 'north')])
    result = aui.scan("north south east")
    assert_equal(result, [('direction', 'north'),
                          ('direction', 'south'),
                          ('direction', 'east')])


def test_verbs():
    assert_equal(aui.scan("go"), [('verb', 'go')])
    result = aui.scan("go kill eat")
    assert_equal(result, [('verb', 'go'),
                          ('verb', 'kill'),
                          ('verb', 'eat')])


def test_stops():
    assert_equal(aui.scan("the"), [('stop', 'the')])
    result = aui.scan("the in of")
    assert_equal(result, [('stop', 'the'),
                          ('stop', 'in'),
                          ('stop', 'of')])


def test_nouns():
    assert_equal(aui.scan("bear"), [('noun', 'bear')])
    result = aui.scan("bear princess")
    assert_equal(result, [('noun', 'bear'),
                          ('noun', 'princess')])


def test_numbers():
    assert_equal(aui.scan("1234"), [('number', 1234)])
    result = aui.scan("3 91234")
    assert_equal(result, [('number', 3),
                          ('number', 91234)])


def test_errors():
    assert_equal(aui.scan("ASDFADFASDF"),
                 [('error', 'ASDFADFASDF')])
    result = aui.scan("bear IAS princess")
    assert_equal(result, [('noun', 'bear'),
                          ('error', 'IAS'),
                          ('noun', 'princess')])
