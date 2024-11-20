from functools import lru_cache
from collections import Counter

# by using @lru_cache decorator we will improve function runtime by caching input and output
@lru_cache(maxsize=100)
def one_char_counter(text: str): #-> int:

    # Raise an Error if input type is not a string, else continue
    if not isinstance(text, str):
        raise TypeError("Input must be a string!")

    # By using 'Counter' method from 'collections' package we count every character and add amount of it in to dictionary
    dict_of_characters = Counter(text)

    # Here by using count method and for loop we can add characters to the list that repeats only once
    single_char_counter = [value for key, value in dict_of_characters.items() if dict_of_characters[key] == 1]

    # return amount of characters in the lis as a result
    return len(single_char_counter)

