from decl import Decl
from globals import tokenizer


class DeclSeq:
    def __init__(self): # <decl seq>	::= <decl> | <decl> <decl seq>
        self.decl = None
        self.decl_seq = None 

    def parse_decl_seq(self):   # Parse decl seq     
        self.decl = Decl() 
        self.decl.parse_decl() 

        # check for more decl's
        # if tokenizer.getToken() == 2:
        #     # 2 = begin, if keyword begin is next that means all the declarations are done
        #     return
        if tokenizer.getToken() != 4:  # Check for "int"
            return
        self.decl_seq = DeclSeq()    
        self.decl_seq.parse_decl_seq()

    def print_decl_seq(self):
        self.decl.print_decl()
        print(";\n")
        if self.decl_seq is not None:
            self.decl_seq.print_decl_seq()

    def exec_decl_seq(self):
        self.decl.exec_decl()
        if self.decl_seq is not None:
            self.decl_seq.exec_decl_seq()