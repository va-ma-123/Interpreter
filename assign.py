import sys
import id
import exp


class Assign:
    # constructor
    def __init__(self, tokenizer = None): # <assign> ::= <id> = <exp>;
        self.tokenizer = tokenizer
        self.id = None
        self.exp = None

    # parse the assign
    def parse_assign(self):
        
        try:
            self.id = self.tokenizer.idVal() #returns the name of the id
            id.Id.parse_id_assign(self.id,self.tokenizer) #parse the id
            if self.tokenizer.getToken() != 14: # 14 is the token for '='
                raise ValueError("'=' Expected")
            self.tokenizer.skipToken() # skip =
            self.exp = exp.Exp(self.tokenizer)
            self.exp.parse_exp() #parse the expression
            id.Id.eIds[self.id].initialized = True #set the id to initialized
            if self.tokenizer.getToken() != 12: # 12 is the token for ';'
                raise ValueError("';' Expected")
            self.tokenizer.skipToken() # skip ;
        except ValueError as e:
            # Handle the error
            print("Error in parse_assign:", e)
            sys.exit(1)

    # execute the assign
    def exec_assign(self):
        val = self.exp.exec_exp() #execute the expression
        id.Id.setValue(self.id,val) #set the value of the id to the value of the expression

    # pretty print the assign
    def print_assign(self, indent=0):
        print("   " * (indent + 1), end="")
        print (self.id, end="")
        print(" = ", end="")
        self.exp.print_exp()
        print(";")