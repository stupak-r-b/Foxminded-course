from functools import cache
from collections import Counter

# my cache decorator with input type checking
def my_cache(func):

    #Checking if the input is a function
    if not callable(func):
        raise TypeError("Input must be a function")

    # Cache the function with @cache decorator
    @cache
    def wrapper(*args, **kwargs):
        return func(*args, **kwargs)
    return wrapper


@my_cache
def one_char_counter(text: str) -> int:

    # Raise an Error if input type is not a string, else continue
    if not isinstance(text, str):
        raise TypeError("Input must be a string!")

    # By using 'Counter' method from 'collections' package we count every character and add amount of it in to dictionary
    dict_of_characters = Counter(text)

    # Here by using count method and for loop we can add characters to the list that repeats only once
    single_char_counter = [value for value in dict_of_characters.values() if value == 1]

    # return amount of characters in the lis as a result
    return len(single_char_counter)
