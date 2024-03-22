from id import Id
import exp as Exp

class Op:
    def __init__(self, tokenizer):
        self.value = None
        self.id = None
        self.exp = None

    def parse_op(self):
        token = self.tokenizer.getToken()
        if token.isdigit():
            self.value = int(token)
        elif token.isalpha():
            self.id = Id(self.tokenizer)
            self.id.parse_id()
        elif token == '(':
            self.tokenizer.skipToken()
            self.exp = Exp(self.tokenizer)
            self.exp.parse_exp()
            if self.tokenizer.getToken() != ')':
                raise ValueError("Expected ')")
            self.tokenizer.skipToken()

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