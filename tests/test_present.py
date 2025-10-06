import pytest
from lib.present import *

""" 
When a new present is wrapped,
It can be unwrapped
"""

def test_present_with_new_present_wrapped():
    present = Present()
    present.wrap('running shorts')
    actual = present.unwrap()
    expected = "running shorts"
    assert actual == expected

""" 
When no present is wrapped,
An message error is received: 'No contents have been wrapped.'
"""

def test_present_when_no_present_has_been_wrapped():
    present = Present()
    with pytest.raises(Exception) as e:
        present.unwrap()
    actual_error_message = str(e.value) 
    expected_error_message = "No contents have been wrapped."
    assert actual_error_message == expected_error_message


""" 
When we already have a wrapped present and we try to wrap another,
An message error is received: 'A contents has already been wrapped.'
"""

def test_present_when_a_present_has_already_been_wrapped():
    present = Present()
    present.wrap("salty peanuts")
    with pytest.raises(Exception) as e:
        present.wrap("umbrella")
    actual_error_message = str(e.value) 
    expected_error_message = "A contents has already been wrapped."
    assert actual_error_message == expected_error_message

""" 
When we already have a wrapped present and we try to wrap another,
The first wrapped message is unchanged.'
"""


def test_wrapping_already_wrapped_preserves_value():
    present = Present()
    present.wrap('running shoes')
    with pytest.raises(Exception) as e:
        present.wrap("umbrella")
    actual =present.unwrap()
    expected = 'running shoes'
    assert actual == expected