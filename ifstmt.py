import sys
import cond 
import stmt_seq as ss

class If:
    # constructor
    def __init__(self, tokenizer = None):
        self.tokenizer = tokenizer
        self.cond = None
        self.ss1 = None
        self.ss2 = None

    # parse the if
    def parse_if(self):
        try: 
            self.tokenizer.skipToken() # skip "if"
            self.cond = cond.Cond(self.tokenizer) # create an instance of the Cond class
            self.cond.parse_cond() #parse the condition

            if self.tokenizer.getToken() != 6: # 6 is the token for "then"
                raise ValueError("'then' Expected")

            self.tokenizer.skipToken() # skip "then"

            self.ss1 = ss.StmtSeq(self.tokenizer)
            self.ss1.parse_stmt_seq() #parse the statement sequence

            if self.tokenizer.getToken() == 7: # 7 is the token for "else"
                self.tokenizer.skipToken() # skip "else"
                self.ss2 = ss.StmtSeq(self.tokenizer)
                self.ss2.parse_stmt_seq() #parse the statement sequence
            
            if self.tokenizer.getToken() != 3: # 3 is the token for "end"
                raise ValueError("'end' Expected")
                
            self.tokenizer.skipToken() # skip "end"
            if self.tokenizer.getToken() != 12:
                raise ValueError("';' Expected")
                
            self.tokenizer.skipToken() # skip ";"
            #print("ENd If: ", tokenizer.getToken())
        except ValueError as e:
            # Handle the error
            print("Error in parse_if:", e)
            sys.exit(1)

    # No execute for if
    def exec_if(self):
        if self.cond.exec_cond():  # execute the condition
            self.ss1.exec_stmt_seq() #execute the statement sequence
            return
        if self.ss2 is not None: # if statement sequence 2 is not none
            self.ss2.exec_stmt_seq() #execute the statement sequence 2
            return
        
    # pretty print the if
    def print_if(self, indent=0):
        print("   " * (indent + 1), end="") # print the indentation
        print("if ", end="") # print "if"
        self.cond.print_cond() # pretty print the condition
        print(" then") # print "then"
        self.ss1.print_stmt_seq(indent + 1) # pretty print the statement sequence
        if self.ss2:
            print("   " * (indent + 1), end="") # print the indentation
            print("else") # print "else"
            self.ss2.print_stmt_seq(indent + 1) # pretty print the statement sequence
        print("   " * (indent + 1), end="") # print the indentation
        print("end;") # print "end;"