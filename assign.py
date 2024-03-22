from id import Id
from exp import Exp

class Assign:
    def __init__(self, tokenizer): # <assign> ::= <id> = <exp>;
        self.tokenizer = tokenizer
        self.id = None
        self.exp = None

    def parse_assign(self):
        self.id = Id(self.tokenizer)
        self.tokenizer.skipToken() # skip identifier
        if self.tokenizer.getToken() != 14:
            print("ERROR: '=' expected")
            return
        self.tokenizer.skipToken() # skip =
        self.exp = Exp(self.tokenizer)
        self.exp.parse_exp()
        if self.tokenizer.getToken() != 12:
            print("ERROR: ';' expected")
            return
        self.tokenizer.skipToken() # skip ;

    def print_assign(self):
        self.id.print_id()
        print(" = ")
        self.exp.print_exp()

    def exec_assign(self):
        val = self.exp.exec_exp()
        self.id.setValue(val)
