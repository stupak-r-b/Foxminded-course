from functools import lru_cache

# by using @lru_cache decorator we will improve function runtime by caching input and output
@lru_cache(maxsize=100)
def one_char_counter(text: str) -> int:

    # Raise an Error if input type is not a string, else continue
    if not isinstance(text, str):
        raise TypeError("Input must be a string!")

    # Here by using count method and for loop we can add characters to the list that repeats only once
    single_char_counter = [char for char in text if text.count(char) == 1]

    # return amount of characters in the lis as a result
    return len(single_char_counter)

