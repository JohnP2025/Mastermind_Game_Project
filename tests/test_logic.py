import sys, os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import mastermind_Logic


def test_invalid1():
    guess = "Pink Orange Cyan"
    colors = colors=["Orange", "Yellow", "Green", "Cyan", "Indigo", "Pink"]
    assert mastermind_Logic.invalid(guess, colors) == True