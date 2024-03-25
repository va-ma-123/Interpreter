from globals import tokenizer
import sys
import id


class Decl:
    def __init__(self): #<decl> ::= int  <id list>;
        self.ids = []

    def parse_decl(self): # Parse decl         
        # Check for "int"
        try:
            if tokenizer.getToken() != 4: 
                raise ValueError("'int' Expected")
            
            tokenizer.skipToken() # skip "int"

            idName = tokenizer.idVal() #gets the name of the id
            #self.id_list = IDList(tokenizer)
            id.Id.parse_id_decl(idName)
            self.ids.append(idName)
            while tokenizer.getToken() != 12:
                if tokenizer.getToken() != 13:
                    if tokenizer.getToken() == 32:                        
                        raise ValueError("Expected ','")
                    else:
                        raise ValueError("Expected ';'") 
                tokenizer.skipToken() # skip ,
                idName = tokenizer.idVal() #gets the name of the id
                #self.id_list = IDList(tokenizer)
                id.Id.parse_id_decl(idName)
                self.ids.append(idName)                    
            
            tokenizer.skipToken() # skip ";"
        except ValueError as e:
            # Handle the error
            print("Error in parse_decl:", e)
            sys.exit(1)

    def exec_decl(self):
        pass

    def print_decl(self, indent=0):
        print("   " * (indent + 1), end="")
        print("int ", end="")
        print(self.ids[0], end="")
        if len(self.ids) > 1:
            for idName in self.ids[1:]:
                print(", ", end="")
                print(idName, end="")
        print(";")