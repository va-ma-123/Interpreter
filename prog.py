from globals import tokenizer
import sys
import stmt_seq as ss
import decl_seq as ds


class Prog:
    def __init__(self): #<prog> ::= program <decl seq> begin <stmt seq> end
        self.ds = None
        self.ss = None
    
    def parse_prog(self): # Parse program 
        try:
            if tokenizer.getToken() != 1:  # Check if the token is "program"
                raise ValueError("'program' Expected")
            
            tokenizer.skipToken()  # Skip "program"
            self.ds = ds.DeclSeq()
            self.ds.parse_decl_seq() # Parse <decl seq>

            # Parse begin
            if tokenizer.getToken() != 2:  # Check if the token is "begin"
                raise ValueError("'begin' Expected")
            
            tokenizer.skipToken()  # Skip "begin"

            self.ss = ss.StmtSeq()
            self.ss.parse_stmt_seq() # Parse <stmt seq>

            if tokenizer.getToken() != 3 and tokenizer.getToken() != 33:
                raise ValueError("'end' Expected")
            tokenizer.skipToken()  # Skip "end"
        except ValueError as e:
            # Handle the error
            print("Error in parse_prog:", e)
            sys.exit(1)

    def exec_prog(self):
        self.ds.exec_decl_seq()
        self.ss.exec_stmt_seq()

    def print_prog(self, indent=0):
        print("program")
        if self.ds:
            self.ds.print_decl_seq(indent + 1)
        print("   " * (indent + 1), end="")
        print("begin")
        self.ss.print_stmt_seq(indent + 1)
        print("   " * (indent + 1), end="")
        print("end")