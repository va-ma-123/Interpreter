import sys
import assign
import ifstmt 
import loop 
import inn 
import out 

class Stmt:
    # constructor
    def __init__(self, tokenizer = None):
        self.tokenizer = tokenizer
        self.assign = None
        self.if_stmt = None
        self.loop = None
        self.in_stmt = None
        self.out_stmt = None

    # parse the statement
    def parse_stmt(self):
        token = self.tokenizer.getToken()  # Fetch the next token
        
        try:
            if token == 5:
                # If the token is 'if', parse if
                self.if_stmt = ifstmt.If(self.tokenizer) # Create an instance of the If class
                self.if_stmt.parse_if() # Parse the if statement
            elif token == 8:
                # If the token is 'while', parse loop
                self.loop = loop.Loop(self.tokenizer) # Create an instance of the Loop class
                self.loop.parse_loop() # Parse the loop statement
            elif token == 10:
                # If the token is 'read', parse in
                self.in_stmt = inn.In(self.tokenizer) # Create an instance of the In class
                self.in_stmt.parse_in() # Parse the in statement
            elif token == 11:
                # If the token is 'write', parse out
                self.out_stmt = out.Out(self.tokenizer) # Create an instance of the Out class
                self.out_stmt.parse_out() # Parse the out statement
            elif token == 32:
                # parse assign
                self.assign = assign.Assign(self.tokenizer) # Create an instance of the Assign class
                self.assign.parse_assign() # Parse the assign statement
            elif token == 33:
                raise ValueError("end Expected")
            else:
                raise ValueError("Invalid statement")
        except ValueError as e:
            # Handle the error
            print("Error in parse_stmt:", e)
            sys.exit(1)
    
    # execute the statement
    def exec_stmt(self):
        if self.assign:
            self.assign.exec_assign() # Execute the assign statement
        elif self.if_stmt:
            self.if_stmt.exec_if() # Execute the if statement
        elif self.loop:
            self.loop.exec_loop() # Execute the loop statement
        elif self.in_stmt:
            self.in_stmt.exec_in() # Execute the in statement
        elif self.out_stmt:
            self.out_stmt.exec_out() # Execute the out statement

    # pretty print the statement
    def print_stmt(self, indent=0):
        # Updated method to print the statement
        if self.assign:
            self.assign.print_assign(indent) # pretty print the assign statement
        elif self.if_stmt:
            self.if_stmt.print_if(indent) # pretty print the if statement
        elif self.loop:
            self.loop.print_loop(indent) # pretty print the loop statement
        elif self.in_stmt:
            self.in_stmt.print_in(indent) # pretty print the in statement
        elif self.out_stmt:
            self.out_stmt.print_out(indent) # pretty print the out statement