from tokenizer import Scanner as Tokenizer
from prog import Prog
from globals import data
import sys



if __name__ == "__main__":
    # Check if two command-line arguments are provided
    if len(sys.argv) != 3:
        print("Usage: py -3 parsetree.py <core_program_file> <data_file>")
        sys.exit(1)
    
    core_program_file = sys.argv[1]
    data_file = sys.argv[2]
    # Create a singleton instance of the Tokenizer
    tokenizer = Tokenizer(core_program_file)
    
    # Open the file in read mode
    with open(data_file, 'r') as file:
        for line in file:
            data.append(int(line.strip()))


    # Create and initialize the Prog class with the singleton Tokenizer
    prog = Prog(tokenizer)
    
    # Parse the program
    prog.parse_prog()
    prog.print_prog()
    prog.exec_prog()

