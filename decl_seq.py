from globals import tokenizer
import decl


class DeclSeq:
    def __init__(self): # <decl seq>	::= <decl> | <decl> <decl seq>
        self.decl = None
        self.decl_seq = None 

    def parse_decl_seq(self):   # Parse decl seq     
        self.decl = decl.Decl() 
        self.decl.parse_decl() 

        if tokenizer.getToken() != 4:  # Check for "int"
            return
        self.decl_seq = DeclSeq()    
        self.decl_seq.parse_decl_seq()

    def exec_decl_seq(self):
        pass

    def print_decl_seq(self, indent=0):
        self.decl.print_decl()
        if self.decl_seq is not None:
            self.decl_seq.print_decl_seq(indent)
