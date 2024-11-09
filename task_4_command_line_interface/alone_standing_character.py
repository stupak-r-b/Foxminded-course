from collections import Counter

# Data base_dictionary. We're store here all the text and counter of characters that don't repeat, provided by user
data_base = {}

# A function that will count and return amount of  characters that don`t repeat
def one_char_counter(text: str):

    # Raise an Error if input type is not a string, else continue
    if not isinstance(text, str):
        raise TypeError("Input must be a string!")

    # Checking the "data_base" if user already provide text before
    if text in data_base:
        return data_base[text]

    # By using 'Counter' method from 'collections' package we count every character and add amount of it in to dictionary
    char_count = Counter(text)

    # Here by using "sum" method and for loop we can find amount of characters that repeats only once
    single_char_counter = sum([char_count[key] for key, value in char_count.items() if char_count[key] == 1])

    # Add a new text that user provide for the first time in to a dictionary
    data_base[text] = single_char_counter
    return data_base[text]

