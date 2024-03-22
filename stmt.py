from assign import Assign
from ifstmt import If
from loop import Loop
from inn import In
from out import Out

class Stmt:
    def __init__(self, tokenizer):
        self.tokenizer = None
        self.assign = None
        self.if_stmt = None
        self.loop = None
        self.in_stmt = None
        self.out_stmt = None

    def parse_stmt(self):
        token = self.tokenizer.getToken()  # Fetch the next token
        if token is None:
            return  # Return if there are no more tokens
        
        if token == 5:
            # If the token is 'if', parse if
            self.if_stmt = If(self.tokenizer)
            self.if_stmt.parse_if()
        elif token == 8:
            # If the token is 'while', parse loop
            self.loop = Loop(self.tokenizer)
            self.loop.parse_loop()
        elif token == 10:
            # If the token is 'read', parse in
            self.in_stmt = In(self.tokenizer)
            self.in_stmt.parse_in()
        elif token == 11:
            # If the token is 'write', parse out
            self.out_stmt = Out(self.tokenizer)
            self.out_stmt.parse_out()
        elif token.isIdentifier():
            # parse assign
            self.assign = Assign(self.tokenizer)
            self.assign.parse_assign()
        else:
            raise ValueError("Invalid statement")
    
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

    def print_stmt(self):
        if self.assign:
            self.assign.print_assign()
        elif self.if_stmt:
            self.if_stmt.print_if()
        elif self.loop:
            self.loop.print_loop()
        elif self.in_stmt:
            self.in_stmt.print_in()
        elif self.out_stmt:
            self.out_stmt.print_out()