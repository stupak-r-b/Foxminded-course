from alone_standing_character import one_char_counter
import unittest


class TestCharCounter(unittest.TestCase):

    def test_char_count_typical(self):
        self.assertEqual(one_char_counter('abbbccdf'), 3)
        self.assertEqual(one_char_counter("bla-bla-bla"), 0)
        self.assertEqual(one_char_counter("Hello world"), 6)

    def test_char_count_atypical(self):
        with self.assertRaises(TypeError):   # Checking if passing an integer raises a TypeError
            one_char_counter(3)
        with self.assertRaises(TypeError):   # Checking if passing a list raises a TypeError
            one_char_counter([4, 3, 6])
        with self.assertRaises(TypeError):   # Checking if passing a None raises a TypeError
            one_char_counter(None)



if __name__ == "__main__":
    unittest.main()