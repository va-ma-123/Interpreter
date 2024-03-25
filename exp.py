import fac

class Exp:
    # constructor
    def __init__(self, tokenizer = None):
        self.tokenizer = tokenizer
        self.fac = None
        self.op = None
        self.exp = None

    # parse the exp
    def parse_exp(self):
        self.fac = fac.Fac(self.tokenizer) # create an instance of the Fac class
        self.fac.parse_fac() # parse the factor
        token = self.tokenizer.getToken() # get the current token
        if(token in (22,23)): # check if the token is '+' or '-'
            if token == 22: # check if the token is '+'
                self.op = 0
            elif token == 23: # check if the token is '-'
                self.op = 1
            self.tokenizer.skipToken() # skip '+' or '-'
            self.exp = Exp(self.tokenizer) # create an instance of the Exp class
            self.exp.parse_exp() # parse the expression

    def exec_exp(self):
        result = self.fac.exec_fac()
        if self.exp:
            if self.op == 0:
                result += self.exp.exec_exp()
            elif self.op == 1:
                result -= self.exp.exec_exp()
        return result
    
        # pretty print the exp
    def print_exp(self):
        self.fac.print_fac() # print the factor
        if self.op is not None:
            print(" ", end="")
            if self.op == 0: # check if the operator is '+'
                print("+", end="") # print '+'
            else:
                print("-", end="") # print '-'
            print(" ", end="") 
            self.exp.print_exp()