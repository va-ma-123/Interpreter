from globals import tokenizer
import sys
import id
import exp

class Op:
    def __init__(self):
        self.value = None
        self.id = None
        self.exp = None

    def parse_op(self):

        try:
            token = tokenizer.getToken()
            if token == 31: # int
                tokenVal = tokenizer.intVal()
                self.value = tokenVal
                tokenizer.skipToken()
            elif token ==32: # id
                self.id = tokenizer.idVal()
                if not id.Id.is_initialized(self.id):
                    raise ValueError(f"ID '{self.id}' not initialized")
                id.Id.parse_id_assign(self.id)
            elif token == 20: # (Exp)
                tokenizer.skipToken()
                self.exp = exp.Exp()
                self.exp.parse_exp()
                if tokenizer.getToken() != 21:
                    raise ValueError("Expected ')")
                tokenizer.skipToken()
        except ValueError as e:
            # Handle the error
            print("Error in parse_op:", e)
            sys.exit(1)

    def exec_op(self):
        if self.id is not None:
            return id.Id.getValue(self.id)
        elif self.exp is not None:
            return self.exp.exec_exp()
        else:
            return self.value
        
    def print_op(self):
        if self.id is not None:
            print (self.id, end="")
        elif self.exp is not None:
            print("(", end="")
            self.exp.print_exp()
            print(")", end="")
        else:
            print(self.value, end="")