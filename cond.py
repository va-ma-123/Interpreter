import sys
import comp

class Cond:
    # constructor
    def __init__(self, tokenizer = None):
        self.tokenizer = tokenizer
        self.comp = None
        self.negation = False
        self.cond1 = None
        self.cond2 = None
        self.andor = None
 
    # parse the condition
    def parse_cond(self):
        try:
            if self.tokenizer.getToken() == 15: # negation
                self.negation = True
                self.tokenizer.skipToken() # skip !
                self.cond1 = Cond(self.tokenizer) # create an instance of the Cond class
                self.cond1.parse_cond() # parse the condition
            elif self.tokenizer.getToken() == 20: # comp
                self.comp = comp.Comp(self.tokenizer)
                self.comp.parse_comp()  # parse the comparison
            elif self.tokenizer.getToken() == 16:
                self.tokenizer.skipToken() # skip [
                self.cond1 = Cond(self.tokenizer)
                self.cond1.parse_cond() # parse the first condition
                if self.tokenizer.getToken() != 18 and self.tokenizer.getToken() != 19: # check if the token is '&&' or '||'
                    raise ValueError("Expected '&&' or '||'")
                if(self.tokenizer.getToken() == 18): # check if the token is '&&'
                    self.andor = 0 
                else:
                    self.andor = 1
                self.tokenizer.skipToken() # skip '&&' or '||'
                self.cond2 = Cond(self.tokenizer) # create an instance of the Cond class
                self.cond2.parse_cond() # parse the second condition
                if self.tokenizer.getToken() != 17: # check if the token is ']'
                    raise ValueError("Expected ']") 
                self.tokenizer.skipToken() # skip ]
            else:
                raise ValueError("Expected a condition")
        except ValueError as e:
            # Handle the error
            print("Error in parse_cond:", e)
            sys.exit(1)
        
    # execute the condition
    def exec_cond(self):
        if self.comp is not None: # check if the comparison is not None
            return self.comp.exec_comp() # execute the comparison
        elif self.negation: # check if the condition is negated
            return not self.cond1.exec_cond() # negate the condition
        elif self.andor == 0: # check if the condition is an '&&'
            return self.cond1.exec_cond() and self.cond2.exec_cond() # execute the '&&' condition
        else: 
            return self.cond1.exec_cond() or self.cond2.exec_cond() # execute the '||' condition
        
    # pretty print the condition
    def print_cond(self):
        if self.comp is not None: # check if the comparison is not None
            self.comp.print_comp() # pretty print the comparison
        elif self.negation: # check if the condition is negated
            print("!", end="")  # print '!'
            self.cond1.print_cond() # pretty print the condition
        elif self.andor == 0: # check if the condition is an '&&'
            print("[", end="") # print '['
            self.cond1.print_cond()  # pretty print the first condition
            print(" && ", end="")  # print '&&'
            self.cond2.print_cond() # pretty print the second condition
            print("]", end="") # print ']'
        else: 
            print("[", end="") # print '['
            self.cond1.print_cond()  # pretty print the first condition
            print(" || ", end="") # print '||'
            self.cond2.print_cond()  # pretty print the second condition
            print("]", end="")       # print ']'  