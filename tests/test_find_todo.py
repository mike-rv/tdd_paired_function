from lib.find_todo import *
import pytest

"""
Given a text which contains #TODO 
It returns a True
"""
def test_todo_returns_true():
    actual = find_todo_in_text("#TODO - go buy some rice")
    expected = True
    assert actual == expected