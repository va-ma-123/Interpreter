import sys
from globals import initialize_globals
import prog

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python program.py <core_program_file> <data_file>")
        sys.exit(1)

    core_program_file = sys.argv[1]
    data_file = sys.argv[2]
    
    initialize_globals(core_program_file, data_file)  # Initialize globals
    
    # Create an instance of the Prog class
    prog_instance = prog.Prog()
    
    # Parse the program
    prog_instance.parse_prog()
    print("\nProgram Execution Output:\n")
    prog_instance.exec_prog()
    print("\nPretty Print Program Output:\n")
    prog_instance.print_prog()
