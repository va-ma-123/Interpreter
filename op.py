from id import Id
import exp as Exp
from globals import tokenizer

class Op:
    def __init__(self):
        self.value = None
        self.id = None
        self.exp = None

    def parse_op(self):
        token = tokenizer.getToken()
        if token == 31:
            self.value = int(token)
            tokenizer.skipToken()
        elif token ==32:
            self.id = Id()
            self.id.parse_id()
        elif token == '(':
            tokenizer.skipToken()
            self.exp = Exp()
            self.exp.parse_exp()
            if tokenizer.getToken() != ')':
                raise ValueError("Expected ')")
            tokenizer.skipToken()

    def print_op(self):
        if self.value is not None:
            print(self.value)
        elif self.id is not None:
            print(self.id.getName())
        elif self.expression is not None:
            print("(", end="")
            self.exp.print_exp()
            print(")", end="")

    def exec_op(self):
        if self.value is not None:
            return self.value
        elif self.id_instance is not None:
            return self.id.getValue()
        elif self.exp is not None:
            return self.exp.exec_exp()