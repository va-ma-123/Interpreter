import sys
import stmt_seq as ss
import decl_seq as ds


class Prog:
    # constructor
    def __init__(self, tokenizer = None):
        self.tokenizer = tokenizer
        self.ds = None
        self.ss = None
    
    # parse the program
    def parse_prog(self): # Parse program 
        try:
            if self.tokenizer.getToken() != 1:  # Check if the token is "program"
                raise ValueError("'program' Expected")
            
            self.tokenizer.skipToken()  # Skip "program"
            self.ds = ds.DeclSeq(self.tokenizer)
            self.ds.parse_decl_seq() # Parse <decl seq>

            # Parse begin
            if self.tokenizer.getToken() != 2:  # Check if the token is "begin"
                raise ValueError("'begin' Expected")
            
            self.tokenizer.skipToken()  # Skip "begin"

            self.ss = ss.StmtSeq(self.tokenizer)
            self.ss.parse_stmt_seq() # Parse <stmt seq>

            if self.tokenizer.getToken() != 3 and self.tokenizer.getToken() != 33:
                raise ValueError("'end' Expected")
            self.tokenizer.skipToken()  # Skip "end"
        except ValueError as e:
            # Handle the error
            print("Error in parse_prog:", e)
            sys.exit(1)

    # execute the program
    def exec_prog(self):
        self.ds.exec_decl_seq() # Execute <decl seq>
        self.ss.exec_stmt_seq() # Execute <stmt seq>

    # pretty print the program
    def print_prog(self, indent=0):
        print("program") # print "program"
        if self.ds: # if <decl seq> exists
            self.ds.print_decl_seq(indent + 1) # pretty print <decl seq> 
        print("   " * (indent + 1), end="") # print the indentation
        print("begin")  # print "begin"
        self.ss.print_stmt_seq(indent + 1) # pretty print <stmt seq>
        print("   " * (indent + 1), end="") # print the indentation
        print("end") # print "end"