from lib.report_length import *

"""
If the word is blueberries,
Return "This string was 11 characters long."
"""

def test_report_length_for_word_blueberries():
    actual = report_length('blueberries')
    expected = "This string was 11 characters long."
    assert actual == expected 

"""
If the word is an empty string,
Return "This string was 0 characters long."
"""

def test_report_length_for_empty_string():
    actual = report_length('')
    expected = "This string was 0 characters long."
    assert actual == expected 

"""
If the word is a one character string,
Return "This string was 1 characters long."
"""

def test_report_length_for_one_letter_word():
    actual = report_length('a')
    expected = "This string was 1 characters long."
    assert actual == expected 

def test_report_length_for_empty_space():
    actual = report_length(' ')
    expected = "This string was 1 characters long."
    assert actual == expected 