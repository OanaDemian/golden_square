from lib.string_builder import *

"""
When we add a single word,
Returns the word and word's length when .output(), .size() are called on the StringBuilder instance 
"""

def test_string_builder_with_single_word():
    string_builder = StringBuilder()
    string_builder.add("Oana")
    actual_string = string_builder.output()
    expected_string = "Oana"
    actual_string_length = string_builder.size()
    expected_string_length = 4
    assert actual_string == expected_string 
    assert actual_string_length == expected_string_length


"""
When we add an empty string',
Returns '' and 0 when .output(), .size() are called on the StringBuilder instance 
"""

def test_string_builder_with_empty_string():
    string_builder = StringBuilder()
    string_builder.add("")
    actual_string = string_builder.output()
    expected_string = ""
    actual_string_length = string_builder.size()
    expected_string_length = 0
    assert actual_string == expected_string 
    assert actual_string_length == expected_string_length

"""
When we add multiple strings',
The output is those string concatenated 
"""

def test_string_builder_with_multiple_strings():
    string_builder = StringBuilder()
    string_builder.add("Oana")
    string_builder.add("add")
    string_builder.add("more")
    string_builder.add("tests!")
    actual_string = string_builder.output()
    expected_string = "Oana add more tests!"
    assert actual_string == expected_string 
"""
When we add multiple strings',
The size is the size of all those strings added 
"""

def test_string_builder_size_when_multiple_strings_added_successively():
    string_builder = StringBuilder()
    string_builder.add("Oana")
    string_builder.add("add")
    string_builder.add("more")
    string_builder.add("tests!")
    actual_string_length = string_builder.size()
    expected_string_length = 21
    assert actual_string_length == expected_string_length 