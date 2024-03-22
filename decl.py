from id import Id

class Decl:
    def __init__(self, tokenizer): #<decl> ::= int  <id list>;
        self.tokenizer = tokenizer
        self.ids = []

    def parse_decl(self): # Parse decl         
        # Check for "int"
        if self.tokenizer.getToken() != 4: 
            print("ERROR: Expected 'int'")
            return
        self.tokenizer.skipToken() # skip "int"

        id = Id(self.tokenizer)
        #self.id_list = IDList(self.tokenizer)
        id.parse_id()
        self.ids.append(id)
        while self.tokenizer.getToken() == 13:
            self.tokenizer.skipToken() # skip ,
            id = Id(self.tokenizer)
            id.parse_id()
            self.ids.append(id)
        if self.tokenizer.getToken() != 12: # Check for ; at end of decl
            print("ERROR: Expected ';'")
            return
        self.tokenizer.skipToken() # skip ";"

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