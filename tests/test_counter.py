from lib.counter import *

"""
if the number is negative -5,
returns  "Counted to -5 so far."
"""

def test_counter():
    counter = Counter()
    counter.add(-5)
    actual = counter.report()
    expectected = "Counted to -5 so far."

"""
if the number is positive 5,
returns  "Counted to 5 so far."
"""

def test_counter():
    counter = Counter()
    counter.add(5)
    actual = counter.report()
    expectected = "Counted to 5 so far."


"""
if the number is 0,
returns  "Counted to 0 so far."
"""

def test_counter():
    counter = Counter()
    counter.add(0)
    actual = counter.report()
    expectected = "Counted to 0 so far."



"""
if the number is a float 9.17,
returns  "Counted to 9.17 so far."
"""

def test_counter():
    counter = Counter()
    counter.add(0)
    actual = counter.report()
    expectected = "Counted to 9.17 so far."