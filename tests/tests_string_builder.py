from lib.string_builder import *

"""
If the added string is the single word 'Oana',
Returns "Oana" and 4 when .output(), .size() are called on the StringBuilder instance 
"""

def test_string_builder():
    string_builder = StringBuilder()
    string_builder.add("Oana")
    actual_string = string_builder.output()
    expected_string = "Oana"
    actual_string_length = string_builder.size()
    expected_string_length = 4
    assert actual_string == expected_string 
    assert actual_string_length == expected_string_length


"""
If the added string is the sentence 'Oana write some tests!',
Returns Oana write some tests!' and 22 when .output(), .size() are called on the StringBuilder instance 
"""

def test_string_builder():
    string_builder = StringBuilder()
    string_builder.add("Oana")
    actual_string = string_builder.output()
    expected_string = "Oana write some tests!"
    actual_string_length = string_builder.size()
    expected_string_length = 22
    assert actual_string == expected_string 
    assert actual_string_length == expected_string_length


"""
If the added string is an empty string',
Returns '' and 0 when .output(), .size() are called on the StringBuilder instance 
"""

def test_string_builder():
    string_builder = StringBuilder()
    string_builder.add("")
    actual_string = string_builder.output()
    expected_string = ""
    actual_string_length = string_builder.size()
    expected_string_length = 0
    assert actual_string == expected_string 
    assert actual_string_length == expected_string_length