from alone_standing_character import one_char_counter
import pytest

# Parametrize testing  with decorator
@pytest.mark.parametrize("a, expected", [
    ("How are you buddy?", 7),
    ("abbbccdf", 3),
    ("", 0)
])
def test_one_char_counter(a, expected):

    """Does this function return the right amount of characters that don't repeat?"""
    assert one_char_counter(a) == expected
