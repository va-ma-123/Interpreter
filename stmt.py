from globals import tokenizer
import sys
import assign
import ifstmt 
import loop 
import inn 
import out 

class Stmt:
    def __init__(self): # <stmt> = <assign>|<if>|<loop>|<in>|<out>
        # these will change depending on which type it is
        self.assign = None
        self.if_stmt = None
        self.loop = None
        self.in_stmt = None
        self.out_stmt = None

    def parse_stmt(self):      
        try:
            token = tokenizer.getToken()  # Fetch the next token  
            if token == 5:
                # If the token is 'if', parse if
                self.if_stmt = ifstmt.If()
                self.if_stmt.parse_if()
            elif token == 8:
                # If the token is 'while', parse loop
                self.loop = loop.Loop()
                self.loop.parse_loop()
            elif token == 10:
                # If the token is 'read', parse in
                self.in_stmt = inn.In()
                self.in_stmt.parse_in()
            elif token == 11:
                # If the token is 'write', parse out
                self.out_stmt = out.Out()
                self.out_stmt.parse_out()
            elif token == 32:
                # parse assign
                self.assign = assign.Assign()
                self.assign.parse_assign()
            elif token == 33:
                raise ValueError("end Expected")
            else:
                raise ValueError("Invalid statement")
        except ValueError as e:
            # Handle the error
            print("Error in parse_stmt:", e)
            sys.exit(1)
    
    def exec_stmt(self):
        if self.assign:
            self.assign.exec_assign()
        elif self.if_stmt:
            self.if_stmt.exec_if()
        elif self.loop:
            self.loop.exec_loop()
        elif self.in_stmt:
            self.in_stmt.exec_in()
        elif self.out_stmt:
            self.out_stmt.exec_out()

    def print_stmt(self, indent=0):
        if self.assign:
            self.assign.print_assign(indent)
        elif self.if_stmt:
            self.if_stmt.print_if(indent)
        elif self.loop:
            self.loop.print_loop(indent)
        elif self.in_stmt:
            self.in_stmt.print_in(indent)
        elif self.out_stmt:
            self.out_stmt.print_out(indent)