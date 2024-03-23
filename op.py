from id import Id
from globals import tokenizer
import exp

class Op:
    def __init__(self):
        self.value = None
        self.id = None
        self.exp = None

    def parse_op(self):

        token = tokenizer.getToken()
        if token == 31:
            tokenVal = tokenizer.intVal()
            self.value = tokenVal
            tokenizer.skipToken()
        elif token ==32:
            self.id = Id()
            self.id.parse_id_assign()
        elif token == 20:
            tokenizer.skipToken()
            self.exp = exp.Exp()
            self.exp.parse_exp()
            if tokenizer.getToken() != 21:
                raise ValueError("Expected ')")
            tokenizer.skipToken()
            
    def print_op(self):
        if self.id is not None:
            print(self.id.getName())
        elif self.exp is not None:
            print("(", end="")
            self.exp.print_exp()
            print(")", end="")
        else:
            print(self.value, end="")

    def exec_op(self):
        if self.id is not None:
            return self.id.getValue()
        elif self.exp is not None:
            return self.exp.exec_exp()
        else:
            return self.value