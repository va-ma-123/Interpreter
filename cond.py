from globals import tokenizer
import sys
import comp

class Cond:
    def __init__(self): # <cond> ::= <comp>|!<cond>|[<cond>&&<cond>]|[<cond>||<cond>]
        self.comp = None
        self.negation = False
        self.cond1 = None
        self.cond2 = None
        self.andor = None

    def parse_cond(self):
        try:
            if tokenizer.getToken() == 15: # negation
                self.negation = True
                tokenizer.skipToken()
                self.cond1 = Cond()
                self.cond1.parse_cond()
            elif tokenizer.getToken() == 20: # comp
                self.comp = comp.Comp()
                self.comp.parse_comp()
            elif tokenizer.getToken() == 16:
                tokenizer.skipToken() # skip [
                self.cond1 = Cond()
                self.cond1.parse_cond()
                if tokenizer.getToken() != 18 and tokenizer.getToken() != 19:
                    raise ValueError("Expected '&&' or '||'")
                if(tokenizer.getToken() == 18): # if it is &&
                    self.andor = 0
                else: # ||
                    self.andor = 1
                tokenizer.skipToken() # skip the && or the ||
                self.cond2 = Cond()
                self.cond2.parse_cond()
                if tokenizer.getToken() != 17:
                    raise ValueError("Expected ']")
                tokenizer.skipToken() # skip ]
            else:
                raise ValueError("Expected a condition")
        except ValueError as e:
            # Handle the error
            print("Error in parse_cond:", e)
            sys.exit(1)
        
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
            print("!", end="") 
            self.cond1.print_cond()
        elif self.andor == 0:
            print("[", end="")
            self.cond1.print_cond() 
            print(" && ", end="") 
            self.cond2.print_cond()
            print("]", end="")
        else: 
            print("[", end="")
            self.cond1.print_cond() 
            print(" || ", end="")
            self.cond2.print_cond() 
            print("]", end="")        