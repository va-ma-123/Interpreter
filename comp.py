from op import Op
from globals import tokenizer

compops = ['!=','==','<','>','<=','>=']

class Comp:
    def __init__(self):
        self.op1 = None
        self.op2 = None
        self.compop = None

    def parse_comp(self):
        if tokenizer.getToken() != 20:
            raise ValueError("Expected '('")
        tokenizer.skipToken()
        self.op1 = Op()
        self.op1.parse_op()
        if 25 <= tokenizer.getToken() <= 30:
            self.compop = tokenizer.getToken() - 25
            tokenizer.skipToken()
            self.op2 = Op()
            self.op2.parse_op()
            if tokenizer.getToken() != 21:
                raise ValueError("Expected ')'")
            tokenizer.skipToken()
        else:
            raise ValueError("Invalid comparison operator")
        
    def print_comp(self):
        print("(")
        self.op1.print_op()
        print(compops[self.compop])
        self.op2.print_op()
        print(")")
    
    def exec_comp(self):
        val1 = self.op1.exec_op()
        print("Val 1 : ",val1)
        val2 = self.op2.exec_op()
        print("Val 2 : ",val2)
        operation = compops[self.compop]
        comp_expr = f"{val1}{operation}{val2}"
        return eval(comp_expr)

            

        