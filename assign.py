from globals import tokenizer
import sys
import id
import exp


class Assign:
    def __init__(self): # <assign> ::= <id> = <exp>;
        self.id = None
        self.exp = None

    def parse_assign(self):
        
        try:
            self.id = tokenizer.idVal() #returns the name of the id
            id.Id.parse_id_assign(self.id) #parse the id
            if tokenizer.getToken() != 14:
                raise ValueError("'=' Expected")
            tokenizer.skipToken() # skip =
            self.exp = exp.Exp()
            self.exp.parse_exp()
            id.Id.eIds[self.id].initialized = True
            if tokenizer.getToken() != 12:
                raise ValueError("';' Expected")
            tokenizer.skipToken() # skip ;
        except ValueError as e:
            # Handle the error
            print("Error in parse_assign:", e)
            sys.exit(1)
        
    def exec_assign(self):
        val = self.exp.exec_exp()
        id.Id.setValue(self.id,val)

    def print_assign(self, indent=0):
        print("   " * (indent + 1), end="")
        print (self.id, end="")
        print(" = ", end="")
        self.exp.print_exp()
        print(";")