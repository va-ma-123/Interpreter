import sys
import cond
import stmt_seq as ss

# Loop class
class Loop:
    def __init__(self, tokenizer = None):
        self.tokenizer = tokenizer
        self.cond = None
        self.ss = None
    # parse the loop
    def parse_loop(self):
        try:
            self.tokenizer.skipToken() # skip "while"
            self.cond = cond.Cond(self.tokenizer)
            self.cond.parse_cond() #parse the condition
            if self.tokenizer.getToken() != 9: # 9 is the token for "loop"
                raise ValueError("'loop' expected")
            self.tokenizer.skipToken() # skip "loop"
            self.ss = ss.StmtSeq(self.tokenizer)
            self.ss.parse_stmt_seq() #parse the statement sequence
            if self.tokenizer.getToken() != 3:
                raise ValueError("'end' expected")
            self.tokenizer.skipToken() # skip "end"
            if self.tokenizer.getToken() != 12:
                raise ValueError("';' expected")
            self.tokenizer.skipToken() # skip ";"
        except ValueError as e:
            # Handle the error
            print("Error in parse_loop:", e) # print the error
            sys.exit(1)

    def exec_loop(self):
        while self.cond.exec_cond(): # execute the condition
            self.ss.exec_stmt_seq() # execute the statement sequence

    def print_loop(self, indent=0):
        print("   " * (indent + 1), end="") # print the indentation
        print("while ", end="") # print "while"
        self.cond.print_cond()  # pretty print the condition
        print(" loop") # print "loop"
        self.ss.print_stmt_seq(indent + 1) # pretty print the statement sequence
        print("   " * (indent + 1), end="") # print the indentation
        print("end;") # print "end;"