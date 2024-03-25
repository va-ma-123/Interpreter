from globals import tokenizer
import sys
import cond
import stmt_seq as ss

class Loop:
    def __init__(self): # <loop>	::=	while <cond> loop <stmt seq> end;
        self.cond = None
        self.ss = None

    def parse_loop(self):
        try:
            tokenizer.skipToken() # skip "while"
            self.cond = cond.Cond()
            self.cond.parse_cond()
            if tokenizer.getToken() != 9:
                raise ValueError("'loop' expected")
            tokenizer.skipToken()
            self.ss = ss.StmtSeq()
            self.ss.parse_stmt_seq()
            if tokenizer.getToken() != 3:
                raise ValueError("'end' expected")
            tokenizer.skipToken()
            if tokenizer.getToken() != 12:
                raise ValueError("';' expected")
            tokenizer.skipToken()
        except ValueError as e:
            # Handle the error
            print("Error in parse_loop:", e)
            sys.exit(1)

    def exec_loop(self):
        while self.cond.exec_cond():
            self.ss.exec_stmt_seq()

    def print_loop(self, indent=0):
        print("   " * (indent + 1), end="")
        print("while ", end="")
        self.cond.print_cond()
        print(" loop")
        self.ss.print_stmt_seq(indent + 1)
        print("   " * (indent + 1), end="")
        print("end;")