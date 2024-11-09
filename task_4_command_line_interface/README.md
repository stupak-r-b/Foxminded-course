Task 4 - CLI (Command-line Interface)

    1. Add a command-line interface to the previous application. Use the standard library module.
    2. Add functional to process a text file. The application has to have two parameters --string or --file 
    

    E.g.

    python collect_framework.py --string “your string”

    python collect_framework.py --file path_to_text_file

    if you passed two parameters, the parameter '--file' should have higher priority. 
    That means the string should be ignored.

    python collect_framework.py  --string “your string” --file path_to_text_file



    Tests
    Tests should have mocks for reading a file and working with passed parameters. 


