from globals import tokenizer
import sys
import cond 
import stmt_seq as ss

class If:
    def __init__(self): # <if> ::= ...im not writing all that
        self.cond = None
        self.ss1 = None
        self.ss2 = None

    def parse_if(self):
        try: 
            tokenizer.skipToken() # skip "if"
            self.cond = cond.Cond()
            self.cond.parse_cond()

            if tokenizer.getToken() != 6:
                raise ValueError("'then' Expected")

            tokenizer.skipToken() # skip "then"

            self.ss1 = ss.StmtSeq()
            self.ss1.parse_stmt_seq()

            # else cannot be expected
            if tokenizer.getToken() == 7:
                tokenizer.skipToken() # skip "else"
                self.ss2 = ss.StmtSeq()
                self.ss2.parse_stmt_seq()
            
            if tokenizer.getToken() != 3:
                raise ValueError("'end' Expected")
                
            tokenizer.skipToken() # skip "end"
            if tokenizer.getToken() != 12:
                raise ValueError("';' Expected")
                
            tokenizer.skipToken() # skip ";"
        except ValueError as e:
            # Handle the error
            print("Error in parse_if:", e)
            sys.exit(1)

 
    def exec_if(self):
        if self.cond.exec_cond():
            self.ss1.exec_stmt_seq()
            return
        if self.ss2 is not None:
            self.ss2.exec_stmt_seq()
            return
        
    def print_if(self, indent=0):
        print("   " * (indent + 1), end="")
        print("if ", end="")
        self.cond.print_cond()
        print(" then")
        self.ss1.print_stmt_seq(indent + 1)
        if self.ss2:
            print("   " * (indent + 1), end="")
            print("else")
            self.ss2.print_stmt_seq(indent + 1)
        print("   " * (indent + 1), end="")
        print("end;")