from lib.greet import *

def test_greet():
    actual = greet('Oana')
    expected = "Hello, Oana!"
    assert actual == expected