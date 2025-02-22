from fac import Fac

class Exp:
    def __init__(self, tokenizer):
        self.tokenizer = tokenizer
        self.fac = None
        self.op = None
        self.exp = None

    def parse_exp(self):
        self.fac = Fac(self.tokenizer)
        self.fac.parse_fac()

        token = self.tokenizer.getToken()
        if(token in (22,23)):
            if token == 22:
                self.op = 0
            elif token == 23:
                self.op = 1
            self.tokenizer.skipToken()
            self.exp = Exp(self.tokenizer)
            self.exp.parse_exp()
        
            

    def print_exp(self):
        self.fac.print_fac()
        if self.op:
            print(" ")
            if self.op==0:
                print("+")
            else:
                print("-")
            self.exp.print_exp()

    def exec_exp(self):
        result = self.fac.exec_fac()
        if self.exp:
            if self.op == 0:
                result += self.exp.exec_exp()
            elif self.op == 1:
                result -= self.exp.exec_exp()
        return result