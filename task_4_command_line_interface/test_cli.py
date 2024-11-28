import unittest
from unittest.mock import patch, mock_open
from command_line_interface import file_reading

class TestCommandLineInterface(unittest.TestCase):

    # Test function "open" that reads data from the file
    @patch("builtins.open", new_callable=mock_open, read_data="Is there any one?")
    def test_read_file(self, mock_file):
        result = file_reading("mock_filename.txt")

        # Assert that the file was opened with the correct filename
        mock_file.assert_called_once_with("mock_filename.txt", "r")

        # Check if the function returns the expected mocked content
        self.assertEqual(result, "Is there any one?")



if __name__ == "__main__":
    unittest.main()