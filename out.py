import sys
import id

class Out:
    # constructor
    def __init__(self, tokenizer = None):
        self.tokenizer = tokenizer
        self.ids = []
    
    # parse the out
    def parse_out(self):
        try:
            self.tokenizer.skipToken()  # skip write

            idName = self.tokenizer.idVal()  # gets the name of the id
            id.Id.parse_id_assign(idName,self.tokenizer)
            self.ids.append(idName)
            while self.tokenizer.getToken() == 13:
                self.tokenizer.skipToken()  # skip ,
                idName = self.tokenizer.idVal()
                id.Id.parse_id_assign(idName,self.tokenizer)
                self.ids.append(idName)
            if self.tokenizer.getToken() != 12:
                raise ValueError("Expected ';'")  # Check for ; at end of decl
            self.tokenizer.skipToken()  # skip ";"
        except ValueError as e:
            # Handle the error
            print("Error in parse_out:", e)
            sys.exit(1)

    # execute the out
    def exec_out(self):
        for idName in self.ids:
            print(idName, end ="") # print the id
            print(" = ", end="") # print " = "
            print(id.Id.getValue(idName)) # print the value of the id

    # pretty print the out
    def print_out(self, indent=0):
            print("   " * (indent + 1), end="") # print the indentation
            print("write ", end="") # print "write"
            print(self.ids[0], end="") # print the first id
            if len(self.ids) > 1: # if there are more than one id
                for id in self.ids[1:]: # loop through the ids
                    print(", ", end="") # print ", "
                    print(id, end="") # print the id
            print(";") # print ";"
