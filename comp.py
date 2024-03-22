from op import Op

compops = ['!=','==','<','>','<=','>=']

class Comp:
    def __init__(self, tokenizer):
        self.tokenizer = tokenizer
        self.op1 = None
        self.op2 = None
        self.compop = None

    def parse_comp(self):
        if self.tokenizer.getToken() != 20:
            raise ValueError("Expected '('")
        self.tokenizer.skipToken()
        self.op1 = Op(self.tokenizer)
        self.op1.parse_op()
        if 25 <= self.tokenizer.getToken() <= 30:
            self.compop = self.tokenizer.getToken() - 25
            self.tokenizer.skipToken()
            self.op2 = Op(self.tokenizer)
            self.op2.parse_op()
            if self.tokenizer.getToken() != 21:
                raise ValueError("Expected ')'")
            self.tokenizer.skipToken()
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
        val2 = self.op2.exec_op()
        operation = compops[self.compop]
        comp_expr = f"{val1}{operation}{val2}"
        return eval(comp_expr)

            

        