from decl_seq import DeclSeq
from stmt_seq import StmtSeq

class Prog:
    def __init__(self, tokenizer): #<prog> ::= program <decl seq> begin <stmt seq> end
        self.tokenizer = tokenizer
        self.ds = None
        self.ss = None

    def parse_prog(self): # Parse program    
        if self.tokenizer.getToken() != 1:  # Check if the token is "program"
            print("ERROR: Expected 'program'")
            return
        
        self.tokenizer.skipToken()  # Skip "program"
        self.ds = DeclSeq(self.tokenizer)
        self.ds.parse_decl_seq() # Parse <decl seq>

        # Parse begin
        if self.tokenizer.getToken() != 2:  # Check if the token is "begin"
            print("ERROR: Expected 'begin'")
            return
        self.tokenizer.skipToken()  # Skip "begin"
        self.ss = StmtSeq(self.tokenizer)
        self.ss.parse_stmt_seq() # Parse <stmt seq>
        
        # Parse "end"
        if self.tokenizer.getToken() != 3:  # Check if the token is "end"
            print("ERROR: Expected 'end'")
            return
        self.tokenizer.skipToken()  # Skip "end"

    def print_prog(self):
        print("program", end="\n\t")
        self.ds.print_decl_seq()
        print("begin", end="\n\t")
        self.ss.print_stmt_seq()
        print("end")

    def exec_prog(self):
        self.ds.exec_decl_seq()
        self.ss.exec_stmt_seq()

