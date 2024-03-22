from op import Op

class Fac:
    def __init__(self, tokenizer):
        self.tokenizer = tokenizer
        self.op = None
        self.fac = None

    def parse_fac(self):
        self.op = Op(self.tokenizer)
        self.op.parse_op()
        if self.tokenizer.get_token() == 24:
            self.tokenizer.skip_token()
            self.fac = Fac(self.tokenizer)
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