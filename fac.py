
from globals import tokenizer
import op

class Fac:
    def __init__(self):
        self.op = None
        self.fac = None

    def parse_fac(self):

        self.op = op.Op()
        self.op.parse_op()
        if tokenizer.getToken() == 24:
            tokenizer.skipToken()
            self.fac = Fac()
            self.fac.parse_fac()

    def print_fac(self):
        self.op.print_op()
        if self.fac:
            print(" * ", end="")
            self.fac.print_fac()

    def exec_fac(self):
        result = self.op.exec_op()
        if self.fac:
            result *= self.fac.exec_fac()
        return result