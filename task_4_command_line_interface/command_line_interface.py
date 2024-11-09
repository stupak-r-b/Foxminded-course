import argparse

# Imported function "one_char_counter" to count characters that don't repeat in the text
from alone_standing_character import one_char_counter

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

# Try to open a file with data provided by useer
try:
    if file_path:
        with open(file_path, 'r') as file:
            content = file.read()

# If there's no such a file rise an ERROR
except FileNotFoundError:
    print("The file does not exist.")

# If user used only --string command
if args.string and not args.file:
    print(f"The amount of alone standing characters in string is {one_char_counter(args.string)}")

# If user used --string and --file command
elif args.string and args.file:
    print(f"The amount of alone standing characters in the string from the file is {one_char_counter(content)}")

# If user used only --file command
elif args.file and not args.string:
    print(f"The amount of alone standing characters in the string from the file is {one_char_counter(content)}")
