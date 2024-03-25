import sys
import id


class Decl:
    # constructor
    def __init__(self, tokenizer = None):
        self.tokenizer = tokenizer
        self.ids = []

    # parse the decl
    def parse_decl(self): # Parse decl         
        # Check for "int"
        try:
            if self.tokenizer.getToken() != 4:  # 4 is the token for "int"
                raise ValueError("'int' Expected")
            
            self.tokenizer.skipToken() # skip "int"

            idName = self.tokenizer.idVal() #gets the name of the id
            #self.id_list = IDList(tokenizer)
            id.Id.parse_id_decl(idName,self.tokenizer) #parse the id
            self.ids.append(idName) #add the id to the list of ids
            while self.tokenizer.getToken() != 12: # 12 is the token for ";"
                if self.tokenizer.getToken() != 13: # 13  is the token for ","
                    if self.tokenizer.getToken() == 32:  # 32 is the token for "="                      
                        raise ValueError("Expected ','")
                    else:
                        raise ValueError("Expected ';'") 
                self.tokenizer.skipToken() # skip ,
                idName = self.tokenizer.idVal() #gets the name of the id
                id.Id.parse_id_decl(idName,self.tokenizer) #parse the id
                self.ids.append(idName) #add the id to the list of ids                     
            
            self.tokenizer.skipToken() # skip ";"
        except ValueError as e:
            # Handle the error
            print("Error in parse_decl:", e)
            sys.exit(1)

    # No execurte for decl
    def exec_decl(self):
        pass

    # pretty print the decl
    def print_decl(self, indent=0):
        print("   " * (indent + 1), end="")
        print("int ", end="")
        print(self.ids[0], end="")
        if len(self.ids) > 1:
            for idName in self.ids[1:]:
                print(", ", end="")
                print(idName, end="")
        print(";")