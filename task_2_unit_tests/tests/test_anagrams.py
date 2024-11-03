# Let's import reverse_words module from anagrams directory
from anagrams.main import reverse_words
import unittest

class TestReverseWords(unittest.TestCase):

    # test typical behavior
    def test_reverse_typical(self):
        self.assertEqual(reverse_words("abcd efgh"), "dcba hgfe")     # checking if "abcd efgh" returns "dcba hgfe"
        self.assertEqual(reverse_words("a1bcd efg!h"), "d1cba hgf!e") # checking if "a1bcd efg!h" returns "d1cba hgf!e"
        self.assertEqual(reverse_words(""), "")                       # checking if "" returns ""

    # test atypical behavior
    def test_reverse_atypical(self):
        with self.assertRaises(TypeError):
            reverse_words(3)            # Checking if passing an integer raises a TypeError
        with self.assertRaises(TypeError):
            reverse_words([1, 2, 3])    # Checking if passing a list raises a TypeError
        with self.assertRaises(TypeError):
            reverse_words(None)         # Checking if passing a None raises a TypeError


if __name__ == "__main__":
    unittest.main()