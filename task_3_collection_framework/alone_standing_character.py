# By using 'shelve' module we can create a simple database
import shelve


# A function that will count and return amount of  characters that don`t repeat
def one_char_counter(text: str) -> int:

    # Data base_dictionary. We're store here all the text and counter of characters that don't repeat, provided by user
    shelf = shelve.open('mydata')

    # Raise an Error if input type is not a string, else continue
    if not isinstance(text, str):
        raise TypeError("Input must be a string!")

    # Checking the "data_base" if user already provide text before
    if text in shelf:
        return shelf[text]

    # Here by using count method and for loop we can add characters to the list that repeats only once
    single_char_counter = [char for char in text if text.count(char) == 1]

    # Add a new text that user provide for the first time in to a dictionary and amount of single characters in it
    shelf[text] = len(single_char_counter)
    return shelf[text]




