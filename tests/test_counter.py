from lib.counter import *

"""
if the number is negative -5,
returns  "Counted to -5 so far."
"""

def test_counter_negative():
    counter = Counter()
    counter.add(-5)
    actual = counter.report()
    expected = "Counted to -5 so far."
    assert actual == expected

"""
if the number is positive 5,
returns  "Counted to 5 so far."
"""

def test_counter_positive():
    counter = Counter()
    counter.add(5)
    actual = counter.report()
    expected = "Counted to 5 so far."
    assert actual == expected


"""
if the number is 0,
returns  "Counted to 0 so far."
"""

def test_counter_zero():
    counter = Counter()
    counter.add(0)
    actual = counter.report()
    expected = "Counted to 0 so far."
    assert actual == expected



"""
if the number is a float 9.17,
returns  "Counted to 0 so far."
"""

def test_counter_float():
    counter = Counter()
    counter.add(0)
    actual = counter.report()
    expected = "Counted to 0 so far."
    assert actual == expected

"""
When we add multiple numbers to the counter,
The sum of those numbers is the final count
"""

def test_counter_adds_multiple_positive_numbers_to_the_count():
    counter = Counter()
    counter.add(10)
    counter.add(120)
    counter.add(12)
    counter.add(1)
    actual = counter.report()
    expected = "Counted to 143 so far."
    assert actual == expected

def test_counter_adds_multiple_positive__and_negative_numbers_to_the_count():
    counter = Counter()
    counter.add(10)
    counter.add(120)
    counter.add(12)
    counter.add(-1)
    actual = counter.report()
    expected = "Counted to 141 so far."
    assert actual == expected