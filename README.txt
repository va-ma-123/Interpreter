Files: all separate files for the non-terminals in the Core grammar
5.txt and 5data.txt - test cases provided just in case
interpreter.py is the main executable
scanner.py which is the provided good Tokenizer code, renamed, no code changed
The names ifstmt and inn were used because if and in are Python keywords and would be confusing.  
globals.py isn't part of the grammar but it exists to handle making a global tokenizer as well as a global data file
To run the code, on Windows it would be: py -3 interpreter.py <core-file-address> <data-file-address>


