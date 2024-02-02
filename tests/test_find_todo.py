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

"""
Given a text which does not contain #TODO 
It returns False
"""
def test_todo_returns_false():
    actual = find_todo_in_text(" - go buy some rice")
    expected = False
    assert actual == expected

"""
given a empty string 
it returns error message "No text given. Please provide text"
"""
def test_todo_returns_error_message_from_empty_str():
    actual = find_todo_in_text("")
    expected = "No text given. Please provide text"
    assert actual == expected

"""
Given a string that contains todo without # 
It returns False
"""
def test_todo_returns_false_with_TODO_but_no_hash():
    actual = find_todo_in_text("TODO - go buy some rice")
    expected = False
    assert actual == expected

"""
Given a non string value
It throws an error
"""
def test_todo_returns_error_message_from_non_str():
    actual = find_todo_in_text(123)
    expected = "Please provide a string value"
    assert actual == expected

"""
Given missing arguments
An error msg is returned
"""
def test_todo_returns_error_message_from_missing_arguments():
    with pytest.raises(Exception) as e:
        find_todo_in_text()
    actual = str(e.value)
    expected = "Missing arguments. Please provide an argument"
    assert actual == expected