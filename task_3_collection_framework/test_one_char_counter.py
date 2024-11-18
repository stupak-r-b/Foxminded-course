from alone_standing_character import one_char_counter

# Testing passing cases
def test_one_char_counter():

    """Does this function return the right amount of characters that don't repeat?"""
    assert one_char_counter("How are you buddy?") == 7
    assert one_char_counter("abbbccdf") == 3
    assert one_char_counter("") == 0

