from comp import Comp

class Cond:
    def __init__(self, tokenizer):
        self.tokenizer = tokenizer
        self.comp = None
        self.negation = False
        self.cond1 = None
        self.cond2 = None
        self.andor = None

    def parse_cond(self):
        if self.tokenizer.getToken() == 15: # negation
            self.negation = True
            self.tokenizer.skipToken()
            self.cond1 = Cond(self.tokenizer)
            self.cond1.parse_cond()
        elif self.tokenizer.getToken() == 20: # comp
            self.comp = Comp(self.tokenizer)
        elif self.tokenizer.getToken() == 16:
            self.tokenizer.skipToken() # skip [
            self.cond1 = Cond(self.tokenizer)
            self.cond1.parse_cond()
            if self.tokenizer.getToken() not in (18,19):
                raise ValueError("Expected '&&' or '||'")
            if(self.tokenizer.getToken() == 18):
                self.andor = 0
            else:
                self.andor = 1
            self.tokenizer.skipToken()
            self.cond2 = Cond(self.tokenizer)
            self.cond2.parse_cond()
            if self.tokenizer.getToken() != 17:
                raise ValueError("Expected ']")
            self.tokenizer.skipToken() # skip ]
        else:
            print("ERROR: not a condition")
            return
        
    def exec_cond(self):
        if self.comp is not None:
            return self.comp.exec_comp()
        elif self.negation:
            return not self.cond1.exec_cond()
        elif self.andor == 0:
            return self.cond1.exec_cond() and self.cond2.exec_cond()
        else: 
            return self.cond1.exec_cond() or self.cond2.exec_cond()
        
    def print_cond(self):
        if self.comp is not None:
            self.comp.print_comp()
        elif self.negation:
            print("!") 
            self.cond1.print_cond()
        elif self.andor == 0:
            self.cond1.print_cond() 
            print(" && ") 
            self.cond2.print_cond()
        else: 
            self.cond1.print_cond() 
            print(" || ")
            self.cond2.print_cond()
        
            
        
