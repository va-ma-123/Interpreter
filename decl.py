from id import Id
from globals import tokenizer


class Decl:
    def __init__(self): #<decl> ::= int  <id list>;
        self.ids = []

    def parse_decl(self): # Parse decl         
        # Check for "int"
        if tokenizer.getToken() != 4: 
            print("ERROR: Expected 'int'")
            return
        tokenizer.skipToken() # skip "int"

        id = Id()
        #self.id_list = IDList(tokenizer)
        id.parse_id()
        self.ids.append(id)
        while tokenizer.getToken() == 13:
            tokenizer.skipToken() # skip ,
            id = Id()
            id.parse_id()
            self.ids.append(id)
        if tokenizer.getToken() != 12: # Check for ; at end of decl
            print("Decl.py line 25 ")
            print (tokenizer.getToken())
            print("ERROR: Expected ';'")
            return
        tokenizer.skipToken() # skip ";"

    def print_decl(self):
        print("int ", end="")
        self.ids[0].print_id()
        if len(self.ids)>1:
            for id in self.ids[1:]:
                print(", ", end="")
                id.print_id()
        print("; ", end="\n")

    def exec_decl(self):
        self.ids[0].exec_id()
        if len(self.ids)>1:
            for id in self.ids[1:]:
                id.exec_id()