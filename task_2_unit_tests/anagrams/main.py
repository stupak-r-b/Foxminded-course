from string import ascii_letters


# create list with separated words from text
def reverse_words(text: str):

    # raise an Error if input type is not a string, else continue
    if not isinstance(text, str):
        raise TypeError("Input must be a string")

    # create list with separated words from text
    separate_words = text.split()

    # here we will store new reversed and updated words
    reversed_words = []

    for word in separate_words:
        # if word doesn't have any non-letter symbol
        if word.isalpha():
            reversed_words.append(word[::-1])
        # if word has a non-letter symbol
        else:
            for symbol in word:
                if symbol not in ascii_letters:
                    # save an index of a non-letter symbol
                    symbol_index = word.index(symbol)
                    # reversed word without a non-letter symbol
                    reversed_word = "".join(symbol for symbol in word[::-1] if symbol in ascii_letters)
                    # assemble a new reversed work with non-letter symbol that staying in place.
                    new_reversed_word = reversed_word[:symbol_index] + symbol + reversed_word[symbol_index:]
                    # add reversed word in to a list
                    reversed_words.append(new_reversed_word)
    # return reversed and assembled text
    return " ".join(reversed_words)


