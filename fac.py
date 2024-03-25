import op

class Fac:
    # constructor
    def __init__(self, tokenizer = None):
        self.tokenizer = tokenizer
        self.op = None
        self.fac = None

    # parse the factor
    def parse_fac(self):

        self.op = op.Op(self.tokenizer) # create an instance of the Op class
        self.op.parse_op() # parse the operand
        if self.tokenizer.getToken() == 24: # check if the token is '*'
            self.tokenizer.skipToken() # skip '*'
            self.fac = Fac(self.tokenizer) # create an instance of the Fac class
            self.fac.parse_fac() # parse the factor


    def exec_fac(self):
        result = self.op.exec_op() # execute the operand
        if self.fac: # check if the factor is not None
            result *= self.fac.exec_fac() # multiply the result by the factor
        return result

    # pretty print the factor
    def print_fac(self):
        self.op.print_op()
        if self.fac:
            print(" * ", end="")
            self.fac.print_fac()