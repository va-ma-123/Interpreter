from id import Id
from exp import Exp
from globals import tokenizer

class Assign:
    def __init__(self): # <assign> ::= <id> = <exp>;
        self.id = None
        self.exp = None

    def parse_assign(self):
        self.id = Id()
        self.id.parse_id_assign()
        if tokenizer.getToken() != 14:
            print("ERROR: '=' expected")
            return
        tokenizer.skipToken() # skip =
        self.exp = Exp()
        self.exp.parse_exp()
        if tokenizer.getToken() != 12:
            print("ERROR: ';' expected")
            return
        tokenizer.skipToken() # skip ;

    def print_assign(self):
        self.id.print_id()
        print(" = ")
        self.exp.print_exp()

    def exec_assign(self):
        val = self.exp.exec_exp()
        self.id.setValue(val)
