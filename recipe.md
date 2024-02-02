# {{PROBLEM}} TODO Function Design Recipe

Copy this into a `recipe.md` in your project and fill it out.

## 1. Describe the Problem

As a user
So that I can keep track of my tasks
I want to check if a text includes the string `#TODO`.

## 2. Design the Function Signature

_Include the name of the function, its parameters, return value, and side effects._

```python
# EXAMPLE

def find_todo_in_text(text):
    """Extracts uppercase words from a string

    Parameters: 
        text: a string containing words (e.g. "hello WORLD")

    Returns:
        boolean of True if TODO is present and False if not present in text e.g True

    Side effects: (state any side effects)
        This function doesn't print anything or have any other side-effects
    """
    pass # Test-driving means _not_ writing any code here yet.
```

## 3. Create Examples as Tests

_Make a list of examples of what the function will take and return._

```python
# EXAMPLE

"""
Given a text which contains #TODO 
It returns a True
"""
find_todo_in_text("hello WORLD #TODO") => [True]

"""
Given two uppercase words
It returns a list with both words
"""
find_todo_in_text("HELLO WORLD") => ["HELLO", "WORLD"]

"""
Given two lowercase words
It returns an empty list
"""
find_todo_in_text("hello world") => []

"""
Given a lower and a mixed case word
It returns an empty list
"""
find_todo_in_text("hello WoRLD") => []

"""
Given a lowercase word and an uppercase word with an exclamation mark
It returns a list with the uppercase word, no exclamation mark
"""
find_todo_in_text("hello WORLD!") => ["WORLD"]

"""
Given an empty string
It returns an empty list
"""
find_todo_in_text("") => []

"""
Given a None value
It throws an error
"""
find_todo_in_text(None) throws an error
```

_Encode each example as a test. You can add to the above list as you go._

## 4. Implement the Behaviour

_After each test you write, follow the test-driving process of red, green, refactor to implement the behaviour._

Here's an example for you to start with:

```python
# EXAMPLE

from lib.extract_uppercase import *

"""
Given a lower and an uppercase word
It returns a list with the uppercase word
"""
def test_extract_uppercase_with_upper_then_lower():
    result = extract_uppercase("hello WORLD")
    assert result == ["WORLD"]
```

Ensure all test function names are unique, otherwise pytest will ignore them!
