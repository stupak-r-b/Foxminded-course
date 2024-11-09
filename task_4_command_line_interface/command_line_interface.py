import argparse
from alone_standing_character import one_char_counter

parser = argparse.ArgumentParser(description="Returns the number of characters in the string occurring only once.")
parser.add_argument('--string', type=str, help="Text for counting characters.")
parser.add_argument('--file', type=str, help="Text from a file for counting characters.")


args = parser.parse_args()
file_path = args.file
try:
    if file_path:
        with open(file_path, 'r') as file:
            content = file.read()
except FileNotFoundError:
    print("The file does not exist.")

if args.string and not args.file:
    print(f"The amount of alone standing characters in string is {one_char_counter(args.string)}")
elif args.string and args.file:
    print(f"The amount of alone standing characters in the string from the file is {one_char_counter(content)}")
elif args.file and not args.string:
    print(f"The amount of alone standing characters in the string from the file is {one_char_counter(content)}")
