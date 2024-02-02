def find_todo_in_text(text= None):
    if text == None:
        raise Exception("Missing arguments. Please provide an argument")
    if text == "":
        return "No text given. Please provide text"
    if not isinstance(text, str):
        return "Please provide a string value"
    split_word_list = text.split()
    return bool([True for word in split_word_list if word == "#TODO"])