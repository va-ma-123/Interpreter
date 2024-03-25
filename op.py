import sys
import id
import exp

class Op:
    # constructor
    def __init__(self, tokenizer = None):
        self.tokenizer = tokenizer
        self.value = None
        self.id = None
        self.exp = None
    
    # parse the op
    def parse_op(self):
        try:
            token = self.tokenizer.getToken() # get the current token
            if token == 31: # int
                tokenVal = self.tokenizer.intVal() # get the value of the int
                self.value = tokenVal
                self.tokenizer.skipToken() # skip the int
            elif token ==32: # id
                self.id = self.tokenizer.idVal() # get the value of the id
                if not id.Id.is_initialized(self.id):
                    raise ValueError(f"ID '{self.id}' not initialized") # Check if the ID is initialized
                id.Id.parse_id_assign(self.id,self.tokenizer) # parse the id
            elif token == 20: # (Exp)
                self.tokenizer.skipToken() # skip (
                self.exp = exp.Exp(self.tokenizer) # create an instance of the Exp class
                self.exp.parse_exp() # parse the expression
                if self.tokenizer.getToken() != 21: # )
                    raise ValueError("Expected ')")
                self.tokenizer.skipToken()
        except ValueError as e:
            # Handle the error
            print("Error in parse_op:", e)
            sys.exit(1)

    # execute the op
    def exec_op(self):
        if self.id is not None:
            return id.Id.getValue(self.id) # get the value of the id
        elif self.exp is not None:
            return self.exp.exec_exp() # execute the expression
        else:
            return self.value
        
    # pretty print the op
    def print_op(self):
        if self.id is not None:
            print (self.id, end="") # print the id
        elif self.exp is not None:
            print("(", end="") # print "("
            self.exp.print_exp() # pretty print the expression
            print(")", end="") # print ")"
        else:
            print(self.value, end="") # print the value