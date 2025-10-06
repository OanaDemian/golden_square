import pytest
from lib.password_checker import *

"""
If a password of 8 or more characters is provided,
Returns true
"""

def test_password_checker_long_password():
    password_checker = PasswordChecker()
    actual = password_checker.check('OpenSesame')
    expected = True
    assert actual == expected

"""
If a password of less than 8 characters is provided,
It raises an exception with the message: "Invalid password, must be 8+ characters."
"""


def test_password_checker_short_password():
    password_checker = PasswordChecker()
    with pytest.raises(Exception) as e:
        password_checker.check('open!!!')
    actual = str(e.value) 
    expected = "Invalid password, must be 8+ characters."
    assert actual == expected

"""
If an empty string password is provided,
It raises an exception with the message: "Invalid password, must be 8+ characters."
"""
def test_password_checker_empty_string_password():
    password_checker = PasswordChecker()
    with pytest.raises(Exception) as e:
        password_checker.check('')
    actual = str(e.value)
    expected = "Invalid password, must be 8+ characters."
    assert actual == expected

"""
If an 8 character string password is provided,
Returns True
"""
def test_password_checker_8_characters_string_password():
    password_checker = PasswordChecker()
    actual = password_checker.check('OpenDoor')
    expected = True
    assert actual == expected