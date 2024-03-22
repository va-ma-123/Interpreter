from decl import Decl

class DeclSeq:
    def __init__(self, tokenizer): # <decl seq>	::= <decl> | <decl> <decl seq>
        self.tokenizer = tokenizer
        self.decl = None
        self.decl_seq = None 

    def parse_decl_seq(self):   # Parse decl seq     
        self.decl = Decl(self.tokenizer) 
        self.decl.parse_decl() 

        # check for more decl's
        # if self.tokenizer.getToken() == 2:
        #     # 2 = begin, if keyword begin is next that means all the declarations are done
        #     return
        if self.tokenizer.getToken() != 4:  # Check for "int"
            return
        self.decl_seq = DeclSeq(self.tokenizer)    
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