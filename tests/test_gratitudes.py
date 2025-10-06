from lib.gratitudes import *


"""
When provided with an empty string,
Returns the string "Be grateful for: "
"""

def test_gratitues_with_empty_string():
    gratitudes = Gratitudes()
    gratitudes.add("")
    actual = gratitudes.format()
    expected = "Be grateful for: "
    assert actual == expected


"""
When one gratitude is added,
Returns the string "Be grateful for: " and gratitude concatenated
"""

def test_gratitues_with_one_gratitude_provided():
    gratitudes = Gratitudes()
    gratitudes.add("friends")
    actual = gratitudes.format()
    expected = "Be grateful for: friends"
    assert actual == expected

"""
When multiple gratitudes are added successively,
Returns the string "Be grateful for: " and gratitudes concatenated and separated by ,
"""

def test_gratitues_with_multiple_gratitude_provided():
    gratitudes = Gratitudes()
    gratitudes.add("friends")
    gratitudes.add("peer group")
    gratitudes.add("coaches")
    actual = gratitudes.format()
    expected = "Be grateful for: friends, peer group, coaches"
    assert actual == expected