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
It returns True
"""
find_todo_in_text("#TODO - go buy some rice") => [True]

"""
Given a text which does not contain #TODO 
It returns False
"""
find_todo_in_text(" - go buy some rice") => [False]

"""
given a empty string 
it returns error message 
"""
find_todo_in_text("") => "No text given. Please provide text"

"""
Given a string that contains todo without # 
It returns False
"""
find_todo_in_text("TODO - go buy some rice") => False

"""
Given a non string value
An error msg is returned
"""
find_todo_in_text(123) throws an error => ["Please provide a string value"]

"""
Given missing arguments
An error msg is returned
"""
def test_todo_returns_error_message_from_missing_arguments():
    find_todo_in_text() = "Missing arguments. Please provide an argument"
   
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
