from globals import tokenizer
import sys
import op

compops = ['!=','==','<','>','<=','>=']

class Comp:
    def __init__(self): # <comp> ::= (<op><comp_op><op>)
        self.op1 = None
        self.op2 = None
        self.compop = None

    def parse_comp(self):
        try:
            tokenizer.skipToken() # skip '('
            self.op1 = op.Op()
            self.op1.parse_op()
            if 25 <= tokenizer.getToken() <= 30:
                self.compop = tokenizer.getToken() - 25
                tokenizer.skipToken()
                self.op2 = op.Op()
                self.op2.parse_op()
                if tokenizer.getToken() != 21:
                    raise ValueError("Expected ')'")
                tokenizer.skipToken()
            else:
                raise ValueError("Invalid comparison operator")
        except ValueError as e:
            # Handle the error
            print("Error in parse_comp:", e)
            sys.exit(1)
    
    def exec_comp(self):
        val1 = self.op1.exec_op()
        val2 = self.op2.exec_op()
        operation = compops[self.compop]
        comp_expr = f"{val1}{operation}{val2}"
        return eval(comp_expr)
    
    def print_comp(self):
        print("(", end="")
        self.op1.print_op()
        print("", compops[self.compop], "", end="")
        self.op2.print_op()
        print(")", end="")