import sys
import op

compops = ['!=','==','<','>','<=','>=']

class Comp:
    # constructor
    def __init__(self, tokenizer = None):
        self.tokenizer = tokenizer
        self.op1 = None
        self.op2 = None
        self.compop = None
    
    # parse the comparison
    def parse_comp(self):
        try:
            self.tokenizer.skipToken() # skip '('
            self.op1 = op.Op(self.tokenizer) # create an instance of the Op class
            self.op1.parse_op() # parse the first operand
            if 25 <= self.tokenizer.getToken() <= 30: # check if the token is a comparison operator
                self.compop = self.tokenizer.getToken() - 25 # get the index of the comparison operator
                self.tokenizer.skipToken() # skip the comparison operator
                self.op2 = op.Op(self.tokenizer) # create an instance of the Op class
                self.op2.parse_op()     # parse the second operand
                if self.tokenizer.getToken() != 21: # check if the token is ')'
                    raise ValueError("Expected ')'")
                self.tokenizer.skipToken() # skip ')'
            else:
                raise ValueError("Invalid comparison operator")
        except ValueError as e:
            # Handle the error
            print("Error in parse_comp:", e)
            sys.exit(1)
    
    # execute the comparison
    def exec_comp(self):
        val1 = self.op1.exec_op() # execute the first operand
        val2 = self.op2.exec_op() # execute the second operand
        operation = compops[self.compop] # get the comparison operator
        comp_expr = f"{val1}{operation}{val2}" # create the comparison expression
        return eval(comp_expr) # evaluate the comparison expression
    
    # pretty print the comparison
    def print_comp(self):
        print("(", end="") # print '('
        self.op1.print_op() # print the first operand
        print("", compops[self.compop], "", end="") # print the comparison operator
        self.op2.print_op() # print the second operand
        print(")", end="") # print ')'