from alone_standing_character import one_char_counter
import pytest

# Expected input checking
@pytest.mark.parametrize("a, expected", [
    ("How are you buddy?", 7),
    ("abbbccdf", 3),
    ("", 0)
])
def test_one_char_counter(a, expected):

    """Does this function return the right amount of characters that don't repeat?"""
    assert one_char_counter(a) == expected

# Unexpected input checking
@pytest.mark.parametrize("a, expected", [
    ([1, 2, 3], TypeError),
    (123, TypeError),
    ({}, TypeError)
])
def test_one_char_counter(a, expected):

    """Does the wrong input type raises TypeError?"""
    with pytest.raises(TypeError):
        one_char_counter(a)
