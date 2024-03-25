import sys
import tokenizer
import prog

# save the arguments
core_program_file = sys.argv[1]
data_file = sys.argv[2]

# define a fucntion that reads data from the data file
def read_global_data(data_file):
    # Read data from the data file
    array_of_dara = []
    
    with open(data_file, 'r') as file:
        for line in file:
            array_of_dara.append(int(line.strip()))
    return array_of_dara

# Global variables
global data_idx
data_idx = 0

global data_arr
data_arr = read_global_data(data_file)

# main function
if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python program.py <core_program_file> <data_file>")
        sys.exit(1)

    # Create an instance of the tokenizer class
    tokenizer = tokenizer.Scanner(core_program_file)
   
    # Create an instance of the Prog class
    prog_instance = prog.Prog(tokenizer)
    
    # Parse the program
    prog_instance.parse_prog()

    # Execute the program
    print("\nProgram Execution Output:\n")
    prog_instance.exec_prog()

    # Pretty print the program
    print("\nPretty Print Program Output:\n")
    prog_instance.print_prog()


