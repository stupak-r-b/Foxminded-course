import argparse

# Imported function "one_char_counter" to count characters that don't repeat in the text
from alone_standing_character import one_char_counter

# Function that reads file with data
def file_reading(path: str) -> str:

    # Try to open a file with data provided by useer
    try:
        if path:
            with open(path, 'r') as file:
                return file.read()

    # If there's no such a file rise an ERROR and terminate the program
    except FileNotFoundError:
        raise SystemExit("The file does not exist.")

# Function that creates a command line interface
def command_line_interface():

    # Created a parser object with name "parser"
    parser = argparse.ArgumentParser(description="Returns the number of characters in the string occurring only once.")

    # Created a "--string" command
    parser.add_argument('--string', type=str, help="Text for counting characters.")

    # Created a "--file" command
    parser.add_argument('--file', type=str, help="Text from a file for counting characters.")

    # Created an "args" object that works with arguments --string and --file
    args = parser.parse_args()

    # Path to the file provided by user trough terminal
    file_path = args.file

    # String from the file if file existing
    content = file_reading(file_path)

    # If user used only --string command returns amount of characters that don't repeat
    if args.string and not args.file:
        return print(one_char_counter(args.string))

    # If user used --string and --file command returns only amount of characters from the file that don't repeat
    elif args.string and args.file:
        return print(one_char_counter(content))

    # If user used only --file command returns amount of characters from the file that don't repeat
    elif args.file and not args.string:
        return print(one_char_counter(content))

if __name__ == "__main__":
    command_line_interface()