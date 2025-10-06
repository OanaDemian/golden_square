from lib.check_codeword import *

""" 
If the codeword is correct,
Returns "Correct! Come in."
"""

""" 
If the codeword has the right first and last letter,
Returns "Close, but nope."
"""

""" 
If the codeword is wrong,
Returns "WRONG!"
"""

def test_with_correct_codeword():
    actual_when_codeword_horse = check_codeword("horse")
    expected_when_horse = "Correct! Come in."
    assert actual_when_codeword_horse == expected_when_horse

def test_with_close_codeword():
    actual_when_codeword_house = check_codeword("house")
    expected_when_house = "Close, but nope."
    assert actual_when_codeword_house == expected_when_house

def test_with_wrong_codeword():
    actual_when_codeword_lobby = check_codeword("lobby")
    expected_when_lobby = "WRONG!"
    assert actual_when_codeword_lobby == expected_when_lobby

"""
If the codewords has the wrong first letter and the right last one,
Returns 'WRONG!
"""
def test_with_wrong_first_letter_and_right_last_letter_codeword():
    actual = check_codeword("mouse")
    expected = "WRONG!"
    assert actual == expected
def test_with_right_first_letter_and_wrong_last_letter_codeword():
    actual = check_codeword("hobby")
    expected = "WRONG!"
    assert actual == expected