from nose.tools import *
import nose_runner


def setup():
    print("SETUP!")


def teardown():
    print("TEAR DOWN!")


def test_basic():
    print("I RAN!", end='')


def test_nose_runner_first_try():
    name = nose_runner.nose_runner.first_try()
    assert name.first_try() == 1
